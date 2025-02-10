import requests
from bs4 import BeautifulSoup
import json

URL = "https://timesofindia.indiatimes.com/"

#fetch the webpage link and save the data to json file
def scrape_times_of_india():

    response = requests.get(URL)

    if response.status_code != 200:
        print(f"Failed to retrieve the page. Status code: {response.status_code}")
        return

    soup = BeautifulSoup(response.text, "html.parser")

    # page title to check if the request is successful
    print("Page Title:", soup.title.text)

#empty list (headlines and links)
    news_data = []
    
    # Find all headlines with links
    articles = soup.find_all("h2")

    for article in articles:
        title = article.text.strip()   #strip= remove space

        # Find the <a> tag inside the <h2> 
        link_tag = article.find("a")
        link = link_tag["href"] if link_tag else None

        # Convert relative URLs to full URLs
        if link and not link.startswith("http"):
            link = f"https://timesofindia.indiatimes.com{link}"

        if title and link:  # Ensure both title and link exist
            news_data.append({
                "title": title,
                "link": link
            })

    # Print scraped data before saving
    print("Scraped Data:", json.dumps(news_data, indent=4, ensure_ascii=False))

    with open("times_of_india_news.json", "w", encoding="utf-8") as file:
        json.dump(news_data, file, ensure_ascii=False, indent=4)

    print("Scraping complete. Data saved in 'times_of_india_news.json'.")

# Run the scraper
scrape_times_of_india()
