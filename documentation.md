# 📖 Project Documentation: Zillow Clone Scraper & Automation

## 1. Introduction
This project demonstrates how to scrape property listings from a **Zillow clone site** and automate the process of submitting the data into a **Google Form** using Selenium.  
It was built as part of my **100 Days of Python** learning journey (Day 53).

---

## 2. Objectives
- Extract property details (price, address, link) from a Zillow clone site.
- Clean and normalize the scraped data.
- Automate Google Form submissions with Selenium.
- Showcase a complete workflow: **Scraping → Cleaning → Automation → Storage**.

---

## 3. System Requirements
- **Python 3.9+**
- Libraries:
  - `beautifulsoup4`
  - `requests`
  - `selenium`
- Browser: Google Chrome (latest version)
- ChromeDriver (compatible with your Chrome version)

---

## 4. Project Structure
```plaintext
📦 Zillow-Clone-Scraper
 ┣ 📜 scraper.py          # Main script (scraping + automation)
 ┣ 📜 requirements.txt    # Dependencies
 ┣ 📜 README.md           # Project overview
 ┣ 📜 LICENSE             # MIT License
 ┣ 📜 .gitignore          # Ignore cache, venv, logs, drivers
 ┣ 📜 form.csv          # Sample output data
 ┣ 📜       # Demo screenshots of Code
 ┗ 📜 documentation.md  # Detailed technical documentation
