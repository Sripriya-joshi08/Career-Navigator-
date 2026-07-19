# Career Navigator — Career Intelligence Platform

A full-stack web application that helps users explore career paths in the Indian IT job market — built end-to-end with Python and Flask.

## Features

- **8 tech career paths** covered, with salary data, growth trends, and role breakdowns
- **AI-powered chatbot** — rule-based, built using Python's `difflib` for fuzzy string matching, enabling context-aware Q&A without relying on any external API
- **Live data visualization** — salary trends and market growth rendered dynamically using Chart.js
- **Zero-login, privacy-first design** — no accounts, no database, all data served in-memory for fast, read-heavy access
- **RESTful architecture** — Flask routes serving structured JSON to a vanilla JavaScript frontend, templated with Jinja2

## Tech Stack

- **Backend:** Python, Flask
- **Frontend:** HTML, CSS, JavaScript
- **Templating:** Jinja2
- **Visualization:** Chart.js

## How to Run

```bash
git clone https://github.com/Sripriya-joshi08/Career-Navigator-.git
cd Career-Navigator-
pip install flask
python app.py
```

Then open `http://localhost:5000` in your browser.

## About

Built as a personal project to explore full-stack development while solving a real problem — helping students and freshers navigate career options in tech without needing to dig through scattered, inconsistent sources.
