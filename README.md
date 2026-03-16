# RenAIssance: End-to-End Spanish HTR Pipeline

This repository contains a state-of-the-art Handwritten Text Recognition (HTR) pipeline developed for the **RenAIssance Project (GSoC 2026)**. The goal is to provide a pipeline that leverages Large Language Models (LLM) or Vision-Language Models (VLM) throughout the entire OCR process, rather than just as a final correction unit.

## 🚀 Key Features
- **VLM-First Approach**: Direct transcription using Gemini 2.5 Flash, specialized in early modern Spanish paleography.
- **Paleographic Awareness**: Prompts designed to identify and preserve "long s" (ſ), archaic orthography, and historical abbreviations.
- **Self-Correcting Pipeline**: A multi-stage process where the LLM performs a second "linguistic pass" to ensure consistency.
- **End-to-End Metrics**: Integrated CER (Character Error Rate) and WER (Word Error Rate) calculation.

## 📁 Project Structure
- `src/`: Core logic for VLM bridge and metrics.
- `notebooks/`: Professional demonstration in `HTR_Pipeline.ipynb`.
- `data/raw/`: Input manuscript scans (contains sample image).
- `data/processed/`: Extracted text outputs.
- `main.py`: Command-line entry point.

## 🛠️ Installation

1. **Clone the repository** (if applicable).
2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
3. **Configure Environment**:
   Create a `.env` file in the root directory:
   ```env
   GEMINI_API_KEY=your_google_api_key_here
   ```

## 📖 Usage
- **Command Line**: Run `python main.py` to process the sample manuscript.
- **Jupyter**: Open `notebooks/HTR_Pipeline.ipynb` for a visual step-by-step breakdown.

## 📊 Evaluation
The pipeline is designed to exceed the **90% accuracy** requirement by combining high-resolution visual recognition with deep linguistic understanding of historical Spanish.

## ✨ Mentors & Contributors
- **Mentors**: Sergei Gleyzer, Xabier Granja, Nicholas Jones, Harrison Meadows, Emanuele Usai.
- **Developed by**: [Your Name/Candidate Name]
