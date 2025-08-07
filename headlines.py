import requests
from bs4 import BeautifulSoup
URL = "https://www.bbc.com/news"
try:
    response = requests.get(URL)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, "html.parser")
    headlines = []
    for tag in soup.find_all(['h2', 'span']):
        text = tag.get_text(strip=True)
        if text and len(text) > 15 and text not in headlines:
            headlines.append(text)
    with open("headlines.txt", "w", encoding="utf-8") as f:
        for i, title in enumerate(headlines, 1):
            f.write(f"{i}. {title}\n")
    print(f"{len(headlines)} headlines saved to 'headlines.txt'")
except requests.exceptions.RequestException as e:
    print(f"error fetching news: {e}")