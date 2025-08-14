import csv
import os
from gtts import gTTS

name = "1"

# --- Ensure output directory exists ---
output_dir = "../2_audio"
os.makedirs(output_dir, exist_ok=True)

csv_path = f"../1_clean-text/{name}.csv"

# --- Read text from CSV ---
# --- Read all text rows from CSV ---
try:
    with open(csv_path, mode='r', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        rows = [row[0].strip() for row in reader if row and row[0].strip()]
        if not rows:
            raise ValueError("CSV is empty or missing text.")
        clean_text = " ".join(rows)
except Exception as e:
    print(f"Error reading from CSV: {e}")
    exit(1)

# --- Convert Text to Speech ---
tts = gTTS(text=clean_text, lang='en')
audio_path = f"{output_dir}/{name}.mp3"
tts.save(audio_path)

print(f"Audio saved to {audio_path}")
