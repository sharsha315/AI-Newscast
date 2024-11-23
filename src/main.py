import time
import gradio as gr
import asyncio
from datetime import datetime
from news_collector import fetch_tech_news_urls
from news_scraper import scrape_news_content
from summarizer import generate_headlines
from speech_generator import NewsReader

class TechNewsReader:
    def __init__(self):
        self.news_reader = NewsReader()
    
    async def process_news(self):
        start_time = time.time()
        
        # Fetch and process news
        urls = fetch_tech_news_urls()
        content_list = await scrape_news_content(urls)
        headlines = generate_headlines(content_list)
        audio_file = self.news_reader.generate_news_audio(headlines)
        
        # Format output
        formatted_headlines = self.format_headlines_as_list(headlines)
        performance_metrics = self.format_metrics(start_time, urls, content_list, headlines)
        
        return formatted_headlines, performance_metrics, audio_file
    
    def format_headlines_as_list(self, headlines):
        formatted_text = "\n".join(f"• {headline}" for headline in headlines)
        return formatted_text
    
    def format_metrics(self, start_time, urls, content_list, headlines):
        metrics = f"""
📊 Performance Metrics:
• News Fetch Time: {time.time() - start_time:.2f} seconds
• URLs Processed: {len(urls)}
• Average Content Length: {sum(len(c) for c in content_list)/len(content_list):.0f} characters
• Headlines Generated: {len(headlines)}
• Last Updated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
        """
        return metrics
    
    def create_interface(self):
        with gr.Blocks(title="AI Newscast") as app:
            gr.Markdown("# AI Newscast")
            gr.Markdown("Get the latest AI and Tech news read to you!")
            
            with gr.Row():
                fetch_button = gr.Button("Fetch Latest News")
            
            with gr.Row():
                headlines_box = gr.TextArea(label="Headlines", interactive=False)
                metrics_box = gr.TextArea(label="System Metrics", interactive=False)
            
            with gr.Row():
                audio_player = gr.Audio(label="News Audio")
            
            fetch_button.click(
                fn=self.process_news,
                outputs=[headlines_box, metrics_box, audio_player]
            )
        
        return app

if __name__ == "__main__":
    news_reader = TechNewsReader()
    app = news_reader.create_interface()
    app.launch()
