import pytesseract
from PIL import Image
import os
from gtts import gTTS
from moviepy import ImageClip, AudioFileClip  # MoviePy 2.x API

name = "1"

# --- Ensure output directory exists ---
output_dir = "../3_video"
os.makedirs(output_dir, exist_ok=True)

audio_path = f"../2_audio/{name}.mp3"
image_path = f"../0_images/{name}.jpg"

# --- Combine Image and Audio into MP4 ---
audio_clip = AudioFileClip(audio_path)
image_clip = ImageClip(image_path, duration=audio_clip.duration)

# Set audio to the image
video_clip = image_clip.with_audio(audio_clip)

# Export video
video_output_path = f"{output_dir}/{name}.mp4"
video_clip.write_videofile(video_output_path, fps=24)

print(f"Video saved as {video_output_path}")
