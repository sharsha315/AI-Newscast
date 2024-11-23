from transformers import pipeline

def clean_and_extract_content(text):
    # Initialize text cleaning pipeline
    extractor = pipeline("text2text-generation", 
                        model="facebook/bart-large-cnn")
    
    prompt = """Extract the main article content from this text, 
    removing any navigation elements, ads, or irrelevant content:
    
    {text}
    """
    
    # Extract relevant content
    cleaned_text = extractor(prompt.format(text=text[:1024]), 
                           max_length=512, 
                           min_length=100)[0]['generated_text']
    
    return cleaned_text

def generate_headlines(content_list):
    # Initialize summarization pipeline
    summarizer = pipeline("summarization", 
                         model="facebook/bart-large-cnn")
    
    headlines = []
    for content in content_list:
        # Clean and extract relevant content
        cleaned_content = clean_and_extract_content(content)
        
        # Generate headline
        summary = summarizer(cleaned_content, 
                           max_length=30, 
                           min_length=10, 
                           do_sample=False)
        
        headlines.append(summary[0]['summary_text'])
    
    return headlines

if __name__ == "__main__":
    # Test the pipeline
    test_content = ["""
    [Navigation Menu]
    HOME | ABOUT | CONTACT
    
    Main Article:
    AI technology is revolutionizing healthcare with breakthrough applications.
    Researchers have developed new algorithms for early disease detection.
    
    [Advertisement]
    Buy now! Limited time offer!
    
    [Footer]
    Copyright 2024
    """]
    
    headlines = generate_headlines(test_content)
    print("Generated Headlines:", headlines)
