# 🗞️ News Headlines Scraper

This Python script scrapes top headlines from a news website using `requests` and `BeautifulSoup`, then saves them to a `.txt` file.

## ✅ Objective
Automate the collection of news headlines from a public website.

## 🛠 Tools Used
- Python
- requests
- BeautifulSoup

## 📁 Files
- `scrape_headlines.py` - Main script to fetch and parse headlines.
- `headlines.txt` - Output file containing extracted headlines.

## 🚀 How to Run

1. **Install required packages** (if not already installed):

   ```bash
   pip install requests beautifulsoup4
   ```

2. **Run the script**:

   ```bash
   python scrape_headlines.py
   ```

3. **Check the output** in `headlines.txt`:

   ```
   1. Ukraine war: Russia launches drone attack on Kyiv
   2. Heatwave alert issued across southern Europe
   ...
   ```

## 💡 Notes
- Default site used: [BBC News](https://www.bbc.com/news)
- You can change the `url` in the script to scrape another news site.
- Make sure the target site allows scraping and check its `robots.txt`.

## 📌 Outcome
A simple CLI automation project demonstrating basic web scraping skills using Python.
