import requests
from bs4 import BeautifulSoup
import csv

def scrape_headlines(url):
    headers = {"User-Agent": "Mozilla/5.0"}
    resp = requests.get(url, headers=headers, timeout=10)
    resp.raise_for_status()
    soup = BeautifulSoup(resp.text, "html.parser")
    headlines = []
    for tag in soup.find_all(["h1", "h2", "h3"]):
        text = tag.get_text(strip=True)
        if text:
            headlines.append(text)
    return headlines

def save_to_csv(headlines, filename="headlines.csv"):
    with open(filename, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["#", "Headline"])
        for i, h in enumerate(headlines, 1):
            writer.writerow([i, h])
    print(f"Saved {len(headlines)} headlines to {filename}")

def main():
    print("=== Python Web Scraper ===
")
    url = input("Enter URL to scrape (e.g. https://example.com): ").strip()
    if not url.startswith("http"):
        url = "https://" + url
    try:
        print(f"
Scraping {url}...")
        headlines = scrape_headlines(url)
        if not headlines:
            print("No headlines found.")
            return
        print(f"
Found {len(headlines)} headlines:
")
        for i, h in enumerate(headlines[:20], 1):
            print(f"  {i}. {h}")
        save = input("
Save to CSV? (y/n): ").strip().lower()
        if save == "y":
            save_to_csv(headlines)
    except requests.RequestException as e:
        print(f"Error fetching page: {e}")

if __name__ == "__main__":
    main()
