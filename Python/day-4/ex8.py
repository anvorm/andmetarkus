import requests
from bs4 import BeautifulSoup

link = "https://www.tallinn.ee/et/linnavalitsus"
response = requests.get(link)
soup = BeautifulSoup(response.text, "html.parser")

kontaktid = soup.find_all("div", class_="template template --image-with-content--one-for-four template--non-tilable")

print(kontaktid)

for kontakt in kontaktid:
    nimi = kontakt.find("span", class_="embedded-entity")
    print(nimi)