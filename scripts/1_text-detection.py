import pytesseract
from PIL import Image
import csv
import os
from gtts import gTTS
from moviepy import ImageClip, AudioFileClip  # MoviePy 2.x API

name = "1"

# --- Ensure output directory exists ---
output_dir = "../1_clean-text"
os.makedirs(output_dir, exist_ok=True)

# --- OCR Step ---
image_path = f"../0_images/{name}.jpg"  # Fixed path to match project structure
img = Image.open(image_path)
raw_text = pytesseract.image_to_string(img, lang='eng', config='--oem 3 --psm 6')

print("=== Raw Detected Text ===")
print(raw_text)

# --- Clean and group text into a sentence ---
# Remove extra whitespace/newlines, join into one string
clean_text = " ".join(raw_text.split())
print("\n=== Cleaned Text for TTS ===")
print(clean_text)

# --- Save clean_text to CSV file ---
csv_filename = f"{output_dir}/{name}.csv"
try:
    with open(csv_filename, mode='w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([clean_text])
    print(f"\nCleaned text saved to {csv_filename}")
except Exception as e:
    print(f"Error saving to CSV: {e}")
