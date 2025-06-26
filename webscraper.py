# import requests
# from bs4 import BeautifulSoup

# # Step 1: Set the target URL
# url = "https://www.hindustantimes.com/latest-news"

# # Step 2: Fetch the HTML content
# response = requests.get(url)
# soup = BeautifulSoup(response.text, "html.parser")

# # Step 3: Extract headlines
# # On HT, headlines are typically in <h3> tags with class 'hdg3'
# headlines = soup.find_all("h3", class_="hdg3")

# # Step 4: Save to a .txt file
# with open("ht_headlines.txt", "w", encoding="utf-8") as f:
#     for idx, h in enumerate(headlines, 1):
#         headline = h.get_text(strip=True)
#         if headline:
#             f.write(f"{idx}. {headline}\n")

# print("✅ Hindustan Times headlines saved to ht_headlines.txt")


import requests
from bs4 import BeautifulSoup

# Step 1: Fetch HTML content
url = "https://www.bbc.com/news"  # Example news site
response = requests.get(url)
html_content = response.text

# Step 2: Parse HTML using BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser')

# Step 3: Find headlines (usually in <h2> tags on BBC)
headlines = soup.find_all('h2')

# Step 4: Extract text and save to .txt file
with open("headlines.txt", "w", encoding='utf-8') as f:
    for idx, h in enumerate(headlines, 1):
        headline_text = h.get_text(strip=True)
        if headline_text:  # Skip empty
            f.write(f"{idx}. {headline_text}\n")

print("✅ Headlines saved to headlines.txt")
