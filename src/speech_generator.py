from TTS.api import TTS
import os

class NewsReader:
    def __init__(self):
        # Initialize TTS
        self.tts = TTS(TTS.list_models()[0])
        self.output_dir = "output"
        os.makedirs(self.output_dir, exist_ok=True)
        
    def generate_news_audio(self, headlines):
        audio_file = os.path.join(self.output_dir, "tech_news.wav")
        
        # Create news script with pauses
        news_script = "Today's Tech News Headlines. \n\n"
        for i, headline in enumerate(headlines, 1):
            news_script += f"Headline {i}: {headline}. \n\n"
        
        # Generate speech
        self.tts.tts_to_file(
            text=news_script,
            speaker=self.tts.speakers[0],
            language="en",
            file_path=audio_file
        )
        return audio_file
