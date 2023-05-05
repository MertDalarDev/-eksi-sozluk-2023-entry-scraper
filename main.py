import requests
from bs4 import BeautifulSoup

# Keep the URLs of all pages in a list
pages = ["https://eksisozluk2023.com/5-mayis-2023-kahramanmaras-secim-anketi--7646489?a=popular&p={}".format(i) for i in range(1, 40)]

entries = []

# For each page
for page in pages:
    response = requests.get(page, headers={'User-Agent': 'Mozilla/5.0'})
    soup = BeautifulSoup(response.text, "html.parser")
    entry_list = soup.find_all("div", class_="content")
    for entry in entry_list:
        entries.append(entry.text)

# Write all entries to eksi.txt
with open("eksi.txt", "w", encoding="utf-8") as f:
    for entry in entries:
        f.write(entry + "\n")
