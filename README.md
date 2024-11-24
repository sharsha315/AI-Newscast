# AI-Newscast

An innovative multimodal AI application that transforms the latest AI/Tech news into an audio news broadcast using advanced language models and speech synthesis.

## 🚀 Features

- Real-time AI/Tech news fetching using `DuckDuckGo`
- Intelligent content extraction with `Crawl4AI`
- Smart headline generation using `facebook/bart-large-cnn`
- Natural speech synthesis with `Coqui TTS`
- User-friendly `Gradio interface`

## 🎥 Demo Video
[![AI Newscast Demo](https://cdn.loom.com/sessions/thumbnails/343b7925f4ef47b89f947cd219c429b2-52bb01924f9aaa87-full-play.gif)](https://www.loom.com/share/343b7925f4ef47b89f947cd219c429b2?sid=fe93df73-799b-404d-a1bd-e1c0f6c74906)

## ⚙️ Technical Architecture

Text → Speech Pipeline:
1. News Collection (DuckDuckGo Search)
2. Content Extraction (Crawl4AI)
3. Headline Generation (HuggingFace)
4. Speech Synthesis (Coqui TTS)

## 📊 Performance Metrics

- Average news fetch time: X seconds
- Response time: X seconds

## 🛠️ Installation

```bash
git clone https://github.com/sharsha315/AI-Newscast
cd AI-Newscast
pip install -r requirements.txt
playwright install
playwright install-deps
```
## Usage

```bash
python src/main.py
```

Access the interface at: http://localhost:7860

## 🎯 Use Cases
- Stay updated with AI news while multitasking
- Accessibility for visually impaired users
- Content creation for tech podcasts
- Educational resource for AI students

## 🌟 Acknowledgments
- Coqui TTS for speech synthesis
- Hugging Face for NLP models
- Gradio for the UI framework