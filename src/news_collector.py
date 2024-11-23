from langchain_community.tools import DuckDuckGoSearchResults
import json

def fetch_tech_news_urls(query="latest news articles on  Generative AI, Artificial Intelligence and LLMs", num_results=3):
    # Initialize search with JSON output format
    search = DuckDuckGoSearchResults(num_results=num_results, output_format="json")
    
    # Get results
    results = search.invoke(query)
    
    # Parse JSON results
    parsed_results = json.loads(results)
    
    # Extract URLs
    urls = [result['link'] for result in parsed_results]
    
    return urls[:3]

# Test the function
if __name__ == "__main__":
    urls = fetch_tech_news_urls()
    print("Fetched URLs:")
    for url in urls:
        print(f"- {url}")
