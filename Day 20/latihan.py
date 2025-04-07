#latihan
import requests
from bs4 import BeautifulSoup
import csv

# 1. Kirim permintaan HTTP ke halaman web
url = "https://quotes.toscrape.com"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

# 2. Ambil semua quote, author, dan tag
quotes = soup.find_all("div", class_="quote")

# Latihan 1: Tampilkan hanya kutipan dari penulis 'Albert Einstein'
print("n\Kutipan dari albert einstein:")
for q in quotes:
    author = q.find("small", class_="author").get_text()
    if author == "Albert Einstein":
        text = q.find("span", class_="text").get_text()
        print(f"{text} - {author}")

# Latihan 2 : Simpan kutipan ke dalam file quotes.txt
with open("quotes.txt", "w", encoding="utf-8") as f:
    for q in quotes:
        text = q.find('span', class_='text').get_text()
        author = q.find('small', class_='author').get_text()
        f.write(f"{text} - {author}")

# Latihan 3 : scapping halaman ke 2
page2_url = "https://quotes.toscrape.com/page/2"
quotes_page2 = []
response_page2 = requests.get(page2_url)
soup_page2 = BeautifulSoup(response_page2.text, "html.parser")

print("\nKutipan halaman 2:")
for q in soup_page2.find_all("div", class_="quote"):
    text = q.find("span", class_="text").get_text()
    author = q.find("small", class_="author").get_text()
    quotes_page2.append((text, author))
    print(f"{text} - {author}")