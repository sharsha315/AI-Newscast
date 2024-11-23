import asyncio
from crawl4ai import AsyncWebCrawler

async def scrape_news_content(urls):
    scraped_contents = []
    
    async with AsyncWebCrawler(verbose=True) as crawler:
        for url in urls:
            result = await crawler.arun(url=url)
            scraped_contents.append(result.markdown)
    
    return scraped_contents

# Test function
async def test_scraping():
    test_urls = [
        "https://hbr.org/2024/11/generative-ai-is-still-just-a-prediction-machine",
        "https://www.technologyreview.com/2024/02/21/1088984/openai-q-star-artificial-general-intelligence/",
        "https://www.wired.com/story/ai-artificial-intelligence-medicine-health-care/"
    ]
    
    contents = await scrape_news_content(test_urls)
    return contents

if __name__ == "__main__":
    contents = asyncio.run(test_scraping())
    # for i, content in enumerate(contents, 1):
    #     print(f"\nArticle {i} Preview:")
    #     print(f"{content[:200]}...\n")
    print(contents)
