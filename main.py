import requests
from bs4 import BeautifulSoup

# Tüm sayfaların URL'lerini bir liste içinde tut
pages = ["https://eksisozluk2023.com/5-mayis-2023-kahramanmaras-secim-anketi--7646489?a=popular&p={}".format(i) for i in range(1, 40)]

# Boş bir liste oluştur
entries = []

# Her sayfa için
for page in pages:
    # Sayfanın HTML kodunu al
    response = requests.get(page, headers={'User-Agent': 'Mozilla/5.0'})
    # BeautifulSoup ile parse et
    soup = BeautifulSoup(response.text, "html.parser")
    # Entryleri bul (div class="content" olanlar)
    entry_list = soup.find_all("div", class_="content")
    # Her entry için
    for entry in entry_list:
        # Entry'nin metnini al ve listeye ekle
        entries.append(entry.text)

# Tüm entryleri eksi.txt dosyasına yaz
with open("eksi.txt", "w", encoding="utf-8") as f:
    for entry in entries:
        f.write(entry + "\n")
