import gradio as gr
import asyncio
from news_collector import fetch_tech_news_urls
from news_scraper import scrape_news_content

async def main():
    urls = fetch_tech_news_urls()
    print("Fetched URLs:")
    for url in urls:
        print(f"- {url}")

    content_list = await scrape_news_content(urls)
    print(content_list)


if __name__ == "__main__":
    # news_reader = TechNewsReader()
    # app = news_reader.create_interface()
    # app.launch()
    main()
    
