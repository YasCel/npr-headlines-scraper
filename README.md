# NPR Headlines Scraper

A Python script that automatically scrapes the latest NPR news headlines daily and saves them into a clean CSV file.  
This project showcases real-world skills in web scraping, data processing, and automation.

---

## 📋 Features

- Fetches top, world, and politics news headlines from NPR's RSS feeds
- Captures headline, summary, published date, and scrape timestamp
- De-duplicates articles across multiple feeds
- Saves structured data to a CSV file inside a `/data` folder
- Fully automated to run daily via `crontab`

---

## 🛠 Technologies Used

- Python 3
- feedparser
- requests
- pandas
- certifi
- crontab (for scheduling automation)

---

## 🚀 How to Run

1. Clone the repository:

```bash
git clone https://github.com/YasCel/npr-headlines-scraper.git
cd npr-headlines-scraper
