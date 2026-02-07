# 📰 NewsFlash X

A modern, high-performance News Aggregator built with Flask and Vanilla JS, featuring AI-powered article summarization and a premium glassmorphic UI.

![NewsFlash Preview](https://via.placeholder.com/1200x600?text=NewsFlash+X+Preview)

## ✨ Features

- **AI-Powered Summaries**: Generate 3-5 line summaries of any article in real-time.
- **Dynamic Content Engine**: SPA-like experience with AJAX navigation and infinite scroll.
- **Premium UI/UX**: Custom glassmorphic design system with support for **Dark Mode**.
- **Real-time Bookmarking**: Save your favorite stories locally for instant access.
- **Responsive Layout**: Optimized for both mobile and desktop reading experiences.
- **Smart Caching**: LocalStorage integration for summaries and bookmarks to ensure high performance.

## 🚀 Tech Stack

- **Backend**: Python, Flask
- **Frontend**: HTML5, Vanilla CSS (Custom Glassmorphism), JavaScript (ES6+)
- **CSS Framework**: Bootstrap 5.3 (Grid and Core Components)
- **API**: NewsAPI (Article fetching)

## 🛠️ Local Setup

1. **Clone the repository**:
   ```bash
   git clone https://github.com/Hrituparno/Flask_News_App.git
   cd Flask_News_App
   ```

2. **Install dependencies**:
   ```bash
   pip install flask requests
   ```

3. **Run the application**:
   ```bash
   python app.py
   ```

4. **Access the App**: Visit `http://127.0.0.1:5000` in your browser.

## 📂 Project Structure

- `app.py`: Main Flask server logic and API routing.
- `Templates/`: Jinja2 templates for the main dashboard and modals.
- `Static/`: Stylesheets featuring the NewsFlash design system.
- `api_push.py`: Custom deployment helper for GitHub automation.

---
Built by **Hrituparno** with 💜 and AI.
