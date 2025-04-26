import os
import requests
import feedparser
import pandas as pd
from datetime import datetime
import certifi

# List of NPR RSS feeds you want to scrape
rss_feeds = {
    "Top News": "https://feeds.npr.org/1001/rss.xml",
    "World News": "https://feeds.npr.org/1004/rss.xml",
    "Politics": "https://feeds.npr.org/1014/rss.xml",
}

headlines = []

for category, url in rss_feeds.items():
    try:
        headers = {"User-Agent": "Mozilla/5.0"}
        response = requests.get(url, headers=headers, verify=certifi.where(), timeout=10)

        if response.status_code != 200:
            print(f"⚠️ Failed to fetch {category} feed: Status code {response.status_code}")
            continue

        feed = feedparser.parse(response.content)
        print(f"✅ {category}: Found {len(feed.entries)} entries.")

        for entry in feed.entries:
            title = entry.title
            link = entry.link
            summary = getattr(entry, "summary", "No summary available.").strip()
            published_date = getattr(entry, "published", "Unknown").strip()
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            headlines.append({
                "Category": category,
                "Headline": title,
                "Link": link,
                "Summary": summary,
                "PublishedDate": published_date,
                "ScrapeTimestamp": timestamp
            })

    except Exception as e:
        print(f"❌ Error fetching {category} feed: {e}")

# De-duplicate by Link
if headlines:
    df = pd.DataFrame(headlines)
    df.drop_duplicates(subset=["Link"], inplace=True)

    # Sort by Category and Timestamp
    df.sort_values(by=["Category", "ScrapeTimestamp"], inplace=True)

    # Ensure data/ directory exists
    os.makedirs("data", exist_ok=True)

    # Save to CSV
    output_path = "data/headlines_rss.csv"
    df.to_csv(output_path, index=False)

    print(f"✅ Saved {len(df)} unique articles across {df['Category'].nunique()} categories to '{output_path}'.")
else:
    print("⚠️ No headlines were collected. Check feeds or connection.")