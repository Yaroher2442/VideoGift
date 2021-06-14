import pyttsx3
import hashlib
from moviepy.editor import *
from api_wrk import get_jpg
import numpy as np
import cv2
from PIL import Image
import librosa
# engine = pyttsx3.init()
# engine.say("Привет как твои дела?")
# engine.runAndWait()

def create_audio(text):
    file_name = hashlib.sha256(text.encode(encoding='utf-8')).hexdigest() + '.mp3'
    if not os.path.exists(file_name):
        engine = pyttsx3.init()
        rate = engine.getProperty('rate')
        engine.setProperty('rate', rate -60)
        engine.say(text)
        engine.save_to_file(text, f'./audio/{file_name}')
        engine.runAndWait()
        return file_name
    else:
        return file_name


def create_vid(text):
    audd = AudioFileClip('./audio/'+create_audio(text))
    print(audd.duration)
    frames=[]
    images=get_jpg(text)
    print(len(images))
    for frame in images:
        decoded = cv2.imdecode(np.frombuffer(frame.getvalue(), np.uint8), -1)
        cv2.imshow('asfas',decoded)
        cv2.waitKey()
        cv2.destroyAllWindows()
        frames.append(ImageClip(decoded).set_duration(audd.duration/len(images)))

    # videoclip2 = videoclip.set_audio(my_audioclip)
    # return clip
    # videoclip=CompositeVideoClip(frames).set_audio(audd)
    final=concatenate_videoclips(frames).set_audio(audd)
    final.write_videofile('test.mp4', fps=10)



if __name__ == '__main__':
    create_vid('Когда мы пойдём гулять?')
    # create_audio('Когда мы пойдём гулять?')
