import requests
from bs4 import BeautifulSoup
import pandas as pd

base_url = "http://books.toscrape.com/catalogue/page-{}.html"
books_data = []

for page in range(1, 6):
    url = base_url.format(page)
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    books = soup.find_all("article", class_="product_pod")

    for book in books:
        title = book.h3.a["title"]
        price = book.find("p", class_="price_color").text.strip().lstrip("£")
        availability = book.find("p", class_="instock availability").text.strip()
        rating = book.p.get("class")[1]

        books_data.append({
            "Title": title,
            "Price (£)": float(price),
            "Availability": availability,
            "Rating": rating
        })

df = pd.DataFrame(books_data)
df.to_csv("books_dataset.csv", index=False)
print("Scraping complete.")