"""
generate_chart.py
Fetches real contribution data from the GitHub GraphQL API and renders
a custom SVG line chart (styled like activity-chart.svg) with monthly totals.

Requires env var GITHUB_TOKEN and GITHUB_USER (set automatically in the
Action, see .github/workflows/activity-chart.yml).
"""

import os
import json
import datetime
import calendar
import urllib.request

GITHUB_USER = os.environ["GITHUB_USER"]
GITHUB_TOKEN = os.environ["GITHUB_TOKEN"]

QUERY = """
query($login: String!) {
  user(login: $login) {
    contributionsCollection {
      contributionCalendar {
        weeks {
          contributionDays {
            date
            contributionCount
          }
        }
      }
    }
  }
}
"""


def fetch_contributions():
    req = urllib.request.Request(
        "https://api.github.com/graphql",
        data=json.dumps({"query": QUERY, "variables": {"login": GITHUB_USER}}).encode(),
        headers={
            "Authorization": f"Bearer {GITHUB_TOKEN}",
            "Content-Type": "application/json",
        },
    )
    with urllib.request.urlopen(req) as resp:
        data = json.load(resp)

    weeks = data["data"]["user"]["contributionsCollection"]["contributionCalendar"]["weeks"]

    monthly = {m: 0 for m in range(1, 13)}
    current_year = datetime.date.today().year
    for week in weeks:
        for day in week["contributionDays"]:
            d = datetime.date.fromisoformat(day["date"])
            if d.year == current_year:
                monthly[d.month] += day["contributionCount"]
    return monthly


def build_svg(monthly):
    months = [calendar.month_abbr[m] for m in range(1, 13)]
    values = [monthly[m] for m in range(1, 13)]

    max_val = max(values) if max(values) > 0 else 1
    # round the axis max up to a nice number
    axis_max = max(50, ((max_val // 50) + 1) * 50)

    # plot area geometry (matches activity-chart.svg layout)
    x0, x1 = 100, 705
    y_top, y_bottom = 60, 310
    n = len(values)
    step = (x1 - x0) / (n - 1)

    def x_at(i):
        return x0 + step * i

    def y_at(v):
        return y_bottom - (v / axis_max) * (y_bottom - y_top)

    points = " ".join(f"{x_at(i):.1f},{y_at(v):.1f}" for i, v in enumerate(values))
    circles = "\n".join(
        f'      <circle cx="{x_at(i):.1f}" cy="{y_at(v):.1f}" r="5"/>' for i, v in enumerate(values)
    )
    x_labels = "\n".join(
        f'      <text x="{x_at(i):.1f}" y="332">{months[i]}</text>' for i in range(n)
    )

    grid_step = axis_max / 6
    y_labels = "\n".join(
        f'      <text x="60" y="{y_at(grid_step * i) + 4:.1f}">{int(grid_step * i)}</text>'
        for i in range(6, -1, -1)
    )
    grid_lines = "\n".join(
        f'      <line x1="{x0}" y1="{y_at(grid_step * i):.1f}" x2="{x1}" y2="{y_at(grid_step * i):.1f}"/>'
        for i in range(1, 7)
    )

    svg = f"""<svg width="760" height="380" viewBox="0 0 760 380" xmlns="http://www.w3.org/2000/svg">
  <rect width="760" height="380" fill="#0d1117"/>
  <text x="380" y="30" text-anchor="middle" fill="#c9d1d9" font-family="Segoe UI, Arial, sans-serif" font-size="18" font-weight="bold">Monthly Contributions ({datetime.date.today().year})</text>
  <g font-family="Segoe UI, Arial, sans-serif">
    <g stroke="#30363d" stroke-width="1">
{grid_lines}
    </g>
    <g fill="#8b949e" font-size="12" text-anchor="end">
{y_labels}
    </g>
    <line x1="{x0}" y1="{y_top}" x2="{x0}" y2="{y_bottom}" stroke="#8b949e" stroke-width="1.5"/>
    <line x1="{x0}" y1="{y_bottom}" x2="{x1}" y2="{y_bottom}" stroke="#8b949e" stroke-width="1.5"/>
    <polyline fill="none" stroke="#a78bfa" stroke-width="3.5" stroke-linejoin="round" stroke-linecap="round" points="
        {points}
      "/>
    <g fill="#a78bfa">
{circles}
    </g>
    <g fill="#8b949e" font-size="12" text-anchor="middle">
{x_labels}
    </g>
  </g>
</svg>
"""
    return svg


if __name__ == "__main__":
    monthly = fetch_contributions()
    svg = build_svg(monthly)
    with open("activity-chart.svg", "w") as f:
        f.write(svg)
    print("activity-chart.svg updated with real contribution data:", monthly)