# Project Name: Book Data Web Scraper

### 1. Project Overview

- **Target Website:** https://books.toscrape.com/
- **Data Fields Extracted:** Title, Price, Rating
- **Tools Used:** Python, requests, BeautifulSoup, pandas

### 2. Setup Instructions

1. Clone this repo:
   `git clone https://github.com/yourusername/book-scraper`

2. Install dependencies:
   `pip install -r requirements.txt`

3. Run script:
   `python scraper.py`

### 3. Challenges & Solutions

One challenge was locating the correct HTML elements
for extracting book titles and prices.
This was solved using the Inspect tool
to identify classes like "product_pod"
and "price_color".
