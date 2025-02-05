import requests
from bs4 import BeautifulSoup
import json

url="https://timesofindia.indiatimes.com/india/maharashtra"

response= requests.get(url)

response.status_code == 200 


soup = BeautifulSoup(response.text, 'html.parser')

articles = [] 
for article in soup.select("div.content a"):
    

    #strip=remove space
    title = article.text.strip()
    link = "https://timesofindia.indiatimes.com" + article["href"]


    #add  data 
    articles.append({"title": title, "link": link})

#save data into JSON file form   
#with= automatically close the file
#w = write format
#indent 4= space
with open("maharashtra_news.json", "w", encoding="utf-8") as file:
        json.dump(articles, file, indent=4, ensure_ascii=False)



if response.status_code == 200:
    print(" Scraping successful! Data saved in 'maharashtra_news.json'.")
else:
     print(" Failed to retrieve the webpage. Status code:", response.status_code)