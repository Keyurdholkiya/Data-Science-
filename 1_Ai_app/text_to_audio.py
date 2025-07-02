from gtts import gTTS
import os

def text_to_speech_file(text: str, folder: str) -> str:
    tts = gTTS(text)
    path = os.path.join("user_uploads", folder)
    os.makedirs(path, exist_ok=True)
    filename = os.path.join(path, "audio.mp3")
    tts.save(filename)
    print(f"{filename}: Audio saved successfully.")
    return filename

# text_to_speech_file("Hey, I am Keyur and this is my AI model", "f7217040-5110-11f0-b11e-f4a78f455836")


