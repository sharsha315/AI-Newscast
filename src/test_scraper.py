import asyncio
from news_scraper import scrape_news_content

# Test URLs
test_urls = [
    "https://www.reuters.com/technology/artificial-intelligence/",
    "https://www.sciencedaily.com/news/computers_math/artificial_intelligence/",
    "https://news.mit.edu/topic/artificial-intelligence2"
]

async def test_scraping():
    print("Starting content scraping...")
    contents = await scrape_news_content(test_urls)
    
    print("\nScraping Results:")
    for i, content in enumerate(contents, 1):
        print(f"\nArticle {i} Content Preview:")
        print(f"{content[:300]}...")  # Print first 300 characters

# Run the test
if __name__ == "__main__":
    asyncio.run(test_scraping())
