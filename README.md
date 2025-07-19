# Web Scraping Task Solution
**Author:** Ritu Singh  
**Date:** 19/07/2025

---

## 📌 Project Overview
This project demonstrates web scraping using Python and BeautifulSoup. The script scrapes quotes, authors, and tags from a sample public website: [quotes.toscrape.com](https://quotes.toscrape.com/).

The collected data is cleaned and saved in a structured CSV file for future analysis.

---

## 🛠 Tools & Libraries Used
- Python 3
- `requests`
- `BeautifulSoup` (bs4)
- `pandas`

---

## 🧠 Script Highlights
```python
# Extract quotes, authors, and tags from the website
url = 'https://quotes.toscrape.com/'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

quotes = soup.find_all('div', class_='quote')
for quote in quotes:
    text = quote.find('span', class_='text').get_text(strip=True)
    author = quote.find('small', class_='author').get_text(strip=True)
    tags = [tag.get_text(strip=True) for tag in quote.find_all('a', class_='tag')]
