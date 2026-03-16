import os
import sys
from dotenv import load_dotenv

# Add src to path
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

from src.pipeline.vlm_bridge import VLMPipeline
from src.utils.metrics import calculate_cer, calculate_wer

def main():
    load_dotenv()
    print("DEBUG: Environment loaded.")
    
    # Check for API key
    api_key = os.getenv("GEMINI_API_KEY")
    print(f"DEBUG: API Key found: {'Yes' if api_key else 'No'}")
    if not api_key:
        print("ERROR: GEMINI_API_KEY not found in .env file.")
        print("Please create a .env file with your GEMINI_API_KEY.")
        return

    # In a real scenario, we'd loop through images in data/raw
    # For this demonstration, we'll assume a sample image is provided
    sample_image = "data/raw/sample_manuscript.jpg"
    
    if not os.path.exists(sample_image):
        print(f"INFO: {sample_image} not found. Creating a placeholder or waiting for user.")
        # We can't actually transcribe without an image
        # Let's mock the flow for now
        print("--- Mocking Pipeline Flow ---")
        mock_transcription = "In el principio era el verbo, y el verbo era con Dios."
        print(f"Transcribed Text: {mock_transcription}")
        
        corrected_text = "En el principio era el Verbo, y el Verbo era con Dios."
        print(f"Corrected Text: {corrected_text}")
        
        # Mock Evaluation
        ground_truth = "En el principio era el Verbo, y el Verbo era con Dios."
        cer = calculate_cer(ground_truth, corrected_text)
        wer = calculate_wer(ground_truth, corrected_text)
        
        print(f"Evaluation Metrics:")
        print(f" - CER: {cer:.4f}")
        print(f" - WER: {wer:.4f}")
        return

    pipeline = VLMPipeline()
    print("DEBUG: Pipeline initialized.")
    
    print(f"Processing {sample_image}...")
    try:
        # Step 1 & 2: VLM-driven Text Recognition
        raw_text = pipeline.transcribe_image(sample_image)
        print("\n--- Raw Transcription ---")
        print(raw_text)
        
        # Step 3: VLM-driven Text Correction
        refined_text = pipeline.correct_text(raw_text)
        print("\n--- Refined Transcription ---")
        print(refined_text)
        
        # Save output
        output_path = "data/processed/transcription.txt"
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(refined_text)
        print(f"\nResults saved to {output_path}")
        
    except Exception as e:
        print(f"Pipeline error: {e}")

if __name__ == "__main__":
    main()
