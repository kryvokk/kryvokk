<h1 align="center">Привет, я kryvokk 👋</h1>
<h3 align="center">Backend Developer • Python & C++ • Qt • Telegram Bots</h3>

<p align="center">
  <img src="https://readme-typing-svg.demolab.com?font=Fira+Code&size=20&pause=1000&color=00FF9C&center=true&vCenter=true&width=500&lines=Backend+Developer;Python+%7C+C%2B%2B;Docker+%2B+Kubernetes;Qt+Applications;Telegram+Bots" alt="Typing SVG" />
</p>

---

### 🚀 Обо мне

- 🔭 Разрабатываю **backend** на **Python** и **C++**
- 🖥 Пишу десктоп-приложения на **Qt**
- 🤖 Создаю **Telegram-ботов**
- 🐘 Работаю с базами данных **PostgreSQL**
- 🐳 Использую **Docker** и **Kubernetes** для деплоя
- 🌱 Постоянно изучаю новое в разработке и системах

---

### 🛠 Стек технологий

<p align="center">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white"/>
  <img src="https://img.shields.io/badge/C++-00599C?style=for-the-badge&logo=cplusplus&logoColor=white"/>
  <img src="https://img.shields.io/badge/Qt-41CD52?style=for-the-badge&logo=qt&logoColor=white"/>
  <img src="https://img.shields.io/badge/PostgreSQL-4169E1?style=for-the-badge&logo=postgresql&logoColor=white"/>
  <img src="https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white"/>
  <img src="https://img.shields.io/badge/Kubernetes-326CE5?style=for-the-badge&logo=kubernetes&logoColor=white"/>
  <img src="https://img.shields.io/badge/Telegram_Bot_API-26A5E4?style=for-the-badge&logo=telegram&logoColor=white"/>
  <img src="https://img.shields.io/badge/Linux-FCC624?style=for-the-badge&logo=linux&logoColor=black"/>
  <img src="https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=git&logoColor=white"/>
</p>

---

### 📊 GitHub статистика

<p align="center">
  <img height="165" src="https://github-readme-stats.vercel.app/api?username=kryvokk&show_icons=true&theme=radical&hide_border=true&count_private=true"/>
  <img height="165" src="https://github-readme-stats.vercel.app/api/top-langs/?username=kryvokk&layout=compact&theme=radical&hide_border=true"/>
</p>

<p align="center">
  <img src="https://github-readme-streak-stats.herokuapp.com/?user=kryvokk&theme=radical&hide_border=true" alt="streak stats"/>
</p>

<p align="center">
  <img src="https://github-readme-activity-graph.vercel.app/graph?username=kryvokk&theme=react-dark&hide_border=true&area=true" alt="activity graph"/>
</p>

---

### 🐍 Contribution Snake

<p align="center">
  <img src="https://raw.githubusercontent.com/kryvokk/kryvokk/output/github-contribution-grid-snake.svg" alt="snake animation"/>
</p>

> Чтобы «змейка» заработала — нужно один раз настроить GitHub Action `Platane/snk` в репозитории `kryvokk/kryvokk` (workflow ниже).

<details>
<summary>⚙️ workflow для змейки (.github/workflows/snake.yml)</summary>

```yaml
name: generate snake

on:
  schedule:
    - cron: "0 */6 * * *"
  workflow_dispatch: {}
  push:
    branches: [ main ]

jobs:
  generate:
    permissions:
      contents: write
    runs-on: ubuntu-latest
    steps:
      - uses: Platane/snk@v3
        with:
          github_user_name: kryvokk
          outputs: |
            dist/github-contribution-grid-snake.svg
            dist/github-contribution-grid-snake-dark.svg?palette=github-dark
      - uses: crazy-max/ghaction-github-pages@v4
        with:
          target_branch: output
          build_dir: dist
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
```
</details>

---

<p align="center">
  <img src="https://komarev.com/ghpvc/?username=kryvokk&label=Profile%20views&color=00FF9C&style=for-the-badge" alt="profile views"/>
</p>
