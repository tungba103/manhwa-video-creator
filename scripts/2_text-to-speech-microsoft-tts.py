import os
import csv
import asyncio
import edge_tts
from googletrans import Translator

name = "1"

# --- Ensure output directory exists ---
output_dir = "../2_audio"
os.makedirs(output_dir, exist_ok=True)

csv_path = f"../1_clean-text/{name}.csv"

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

# --- Translate to Vietnamese ---
translator = Translator()
translated = translator.translate(clean_text, src='en', dest='vi').text
print(f"Translated to Vietnamese: {translated}")

# --- Convert to Speech (Vietnamese voice) ---
async def tts_vietnamese(text, filename):
    voice = "vi-VN-HoaiMyNeural"  # Vietnamese female voice
    communicate = edge_tts.Communicate(text, voice)
    await communicate.save(filename)

audio_path = f"{output_dir}/{name}.mp3"
asyncio.run(tts_vietnamese(translated, audio_path))

print(f"Audio saved to {audio_path}")
