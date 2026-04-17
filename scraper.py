import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

# Target website
url = "https://books.toscrape.com/"

# Send request
response = requests.get(url)

# Parse HTML
soup = BeautifulSoup(response.text, "html.parser")

# Store data
books_data = []

# Find books
books = soup.find_all("article", class_="product_pod")

# Loop through books
for book in books:

    # Get title
    title = book.h3.a["title"]

    # Get price
    price = book.find("p", class_="price_color").text

    # Get rating
    rating = book.p["class"][1]

    books_data.append({
        "Title": title,
        "Price": price,
        "Rating": rating
    })

# Convert to dataframe
df = pd.DataFrame(books_data)

# Save CSV
df.to_csv("data.csv", index=False)

# Ethical delay
time.sleep(1)

print("Data saved to data.csv")