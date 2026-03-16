import google.generativeai as genai
import PIL.Image
import os
from dotenv import load_dotenv

load_dotenv()

class VLMPipeline:
    def __init__(self, model_name="gemini-2.5-flash"):
        api_key = os.getenv("GEMINI_API_KEY")
        if not api_key:
            raise ValueError("GEMINI_API_KEY not found in environment variables.")
        
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel(model_name)
        
    def transcribe_image(self, image_path, prompt=None):
        """
        Transcribes handwritten text from an image using VLM.
        """
        if not prompt:
            prompt = (
                "You are a world-class paleographer and expert in Early Modern Spanish (16th-17th century). "
                "Analyze the provided handwritten manuscript image. "
                "1. Identify the layout and reading order. "
                "2. Transcribe the text exactly as written, preserving archaic orthography. "
                "3. Pay close attention to historical characters like 'long s' (ſ), 'v' used for 'u' (and vice-versa), "
                "and common abbreviations (e.g., 'q' for 'que'). "
                "4. If text is damaged, use brackets [?] for unclear parts. "
                "Return the transcription text only, formatted with original line breaks."
            )
            
        img = PIL.Image.open(image_path)
        response = self.model.generate_content([prompt, img])
        return response.text

    def correct_text(self, transcription):
        """
        Second pass for linguistic correction and interpretation.
        """
        prompt = (
            "The following is a raw transcription of an early modern Spanish manuscript. "
            "Correct any obvious transcription errors while maintaining archaic spelling conventions. "
            "If a word is unclear, provide your best estimate in brackets [?]. "
            "Original text:\n\n" + transcription
        )
        response = self.model.generate_content(prompt)
        return response.text

if __name__ == "__main__":
    # Example usage (will fail without key/image)
    try:
        pipeline = VLMPipeline()
        print("Pipeline initialized successfully.")
    except Exception as e:
        print(f"Initialization check: {e}")
