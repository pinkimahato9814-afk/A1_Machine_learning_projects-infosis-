# i want to learn about web scrapping
# code for web scrapping using beautifulsoup4 and requests library.
#  This code will scrap news from the website 
from bs4 import BeautifulSoup
import requests


class BsScraper:
    def __init__(self):
        self.target_url = "https://www.sidhakura.com/policy?page="
        self.news_list = []
  
    def scrap_page(self, page=1):
        response = requests.get(f"{self.target_url}{page}")
        html_text = response.text
        soup = BeautifulSoup(html_text, "html.parser")

        full_news_div = soup.find("div", {"class": "full-samachar-list"})

        if full_news_div:
            for i in full_news_div.find_all("div"):
                title_tag = i.find("h2")
                image_tag = i.find("img")
                date_tag = i.find("span")

                if title_tag and image_tag and date_tag:
                    title = title_tag.find("a").text.strip()
                    image = image_tag.get("data-src")
                    publish_date = date_tag.text.strip()

                    self.news_list.append({
                        "title": title,
                        "image": image,
                        "publish_date": publish_date,
                    })

                    print(f"""
TITLE :: {title}
IMAGE :: {image}
PUBLISHED :: {publish_date}
""")

    def scrap_all(self):
        for i in range(1, 10):
            self.scrap_page(i)


# Create instance
instance = BsScraper()
instance.scrap_all()

print(f"TOTAL NEWS SCRAPED: {len(instance.news_list)}")


# import pandas as pd

# # Create DataFrame
# df = pd.DataFrame(instance.news_list)

# # Display data
# print(df)

# # Total rows
# print("Total rows:", len(df))