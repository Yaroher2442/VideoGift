import pyttsx3
import hashlib
from moviepy.editor import *



# engine = pyttsx3.init()
# engine.say("Привет как твои дела?")
# engine.runAndWait()
def create_audio(text):
    file_name = hashlib.sha256(text.encode(encoding='utf-8')).hexdigest() + '.mp3'
    engine = pyttsx3.init()
    engine.save_to_file(file_name, f'./audio/{file_name}')
    engine.runAndWait()
    return file_name

def create_vid(img_path):
    clip = ImageClip(img_path).set_duration(2)
    return clip


if __name__ == '__main__':
    print(create_audio('привеет'))
