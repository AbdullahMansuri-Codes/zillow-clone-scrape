# 🏡 Zillow Clone Web Scraping & Automation Project

![Python](https://img.shields.io/badge/Python-3.9%2B-blue)
![BeautifulSoup](https://img.shields.io/badge/BeautifulSoup-✓-green)
![Selenium](https://img.shields.io/badge/Selenium-Automation-orange)
![Status](https://img.shields.io/badge/Project-Day%2053-success)
![License](https://img.shields.io/badge/License-MIT-lightgrey)

---

## 📌 Overview
This project is part of my **100 Days of Python** learning journey (Day 53).  
It demonstrates how to **scrape property listings from a Zillow clone site** and then **automate Google Form submissions** using Selenium.  

The repo is structured like a mini-course project: you’ll see the scraping phase, automation phase, and improvements, all documented step by step.

---

## 🎯 Learning Outcomes
By completing this project, you will:
- Understand how to use **BeautifulSoup** for web scraping.  
- Learn to clean and normalize scraped data (prices, addresses, links).  
- Automate repetitive tasks with **Selenium WebDriver**.  
- Practice error handling and workflow design.  
- Build a pipeline: **Scraping → Cleaning → Automation → Storage**.  

---

## 🏗️ Course Structure (Day 53 Project)
### Module 1: Web Scraping with BeautifulSoup
- Fetch HTML content using `requests`.  
- Parse DOM with `BeautifulSoup`.  
- Extract property prices, addresses, and links.  
- Clean data (remove `+`, strip whitespace, normalize URLs).  

### Module 2: Automation with Selenium
- Launch Chrome browser with Selenium.  
- Locate Google Form fields using XPath.  
- Fill in scraped data (address, price, link).  
- Submit the form and repeat for all listings.  

### Module 3: Error Handling & Optimization
- Use `WebDriverWait` instead of `time.sleep()`.  
- Wrap automation in `try/except` blocks.  
- Handle runtime issues gracefully.  

### Module 4: Improvements & Extensions
- Add pagination support for scraping multiple pages.  
- Export scraped data to CSV/Excel before automation.  
- Integrate Google Sheets API for direct uploads.  
- Modularize code into functions/classes for scalability.  

---

## 🛠️ Tech Stack
- [Python](https://www.python.org/)  
- [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/)  
- [Requests](https://docs.python-requests.org/)  
- [Selenium](https://www.selenium.dev/)  
- Google Forms  

---

---

## ⚙️ Setup & Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/AbdullahMansuri-Codes/zillow-clone-scraper.git
   cd zillow-clone-scraper

## 📂 Project Structure
📦 Zillow-Clone-Scraper
 ┣ 📜 scraper.py          # Main script (scraping + automation)
 ┣ 📜 requirements.txt    # Dependencies (to be added)
 ┣ 📜 README.md           # Project documentation
 ┣ 📜 LICENSE             # MIT License (to be added)
 ┣ 📜 .gitignore          # Ignore cache, venv, logs (to be added)
 ┣ 📂 data/               # (Optional) Store scraped data backups
 ┣ 📂 screenshots/        # (Optional) Demo screenshots
 ┗ 📂 docs/               # (Optional) Extra documentation

