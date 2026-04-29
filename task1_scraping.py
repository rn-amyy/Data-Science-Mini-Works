import requests
from bs4 import BeautifulSoup
import csv

link="https://quotes.toscrape.com/"
raw=requests.get(link)
soup=BeautifulSoup(raw.text,"html.parser")
with open("quotes.csv","w",newline="",encoding="utf-8") as file:
    writer=csv.writer(file)
    writer.writerow(["Quote","Author","Tag"])
    quotes=soup.find_all("div",class_="quote")

    for quote in quotes:
        name=quote.find("span",class_="text").text
        author=quote.find("small",class_="author").text
        tags_list=[t.text for t in quote.find_all("a",class_="tag")]
        tag=",".join(tags_list)

        writer.writerow([name,author,tag])

print("Data scraped successfully")