# day 20 : Web scraping dengan beautifulsoup

import requests
from bs4 import BeautifulSoup
import csv

# 1. Kirim permintaan HTTP ke halaman web
url = "https://quotes.toscrape.com"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

# 2. Ambil semua quote, author, dan tag
quotes = soup.find_all("div", class_="quote")

# 3. Simpan ke file CSV
with open("quotes.csv", mode="w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Kutipan", "Penulis", "Tags"])

    print("Daftar Kutipan:")
    for q in quotes:
        text = q.find("span", class_="text").get_text()
        author = q.find("small", class_="author").get_text()
        tags = [tag.get_text() for tag in q.find_all("a", class_="tag")]
        tags_str = ", ".join(tags)
        print(f"{text} - {author} [{tags_str}]")
        writer.writerow([text, author, tags_str])


