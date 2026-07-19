from gtts import gTTS
import os
import uuid

AUDIO_FOLDER = "audio"

os.makedirs(AUDIO_FOLDER, exist_ok=True)

def generate_audio(text):

    filename = f"{uuid.uuid4()}.mp3"

    path = os.path.join(AUDIO_FOLDER, filename)

    tts = gTTS(
        text=text,
        lang="en",
        slow=False
    )

    tts.save(path)

    return path