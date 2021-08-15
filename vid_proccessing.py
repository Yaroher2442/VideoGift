import os

import pyttsx3
import hashlib
from moviepy.editor import *
import requests
import shutil
import uuid
import cv2

GAPI_KEY = 'AIzaSyAI52k1NjCXVyJTnDuWAC1b94BCAnit7NQ'


def get_img(text, u_uid):
    js = requests.get(
        f'https://www.googleapis.com/customsearch/v1?q={text}&cx=448c512f7ed8a5a3d&key={GAPI_KEY}&lr=lang_ru&searchType=image').json()
    r = requests.get(js['items'][0]['link'], stream=True)
    if r.status_code == 200:
        with open(f'{u_uid}/img_buf.jpg', 'wb') as f:
            r.raw.decode_content = True
            shutil.copyfileobj(r.raw, f)


def create_audio(text, u_uid):
    file_name = hashlib.sha256(text.encode(encoding='utf-8')).hexdigest() + '.mp3'
    engine = pyttsx3.init()
    engine.save_to_file(text, f'{u_uid}/audio/{file_name}')
    engine.runAndWait()
    return f'{u_uid}/audio/{file_name}'


def create_vid(u_uid, audio_path):
    audio = AudioFileClip(audio_path)
    print(audio.duration)
    image = cv2.imread(f'{u_uid}/img_buf.jpg')
    im_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    clip = ImageClip(im_rgb).set_duration(audio.duration).set_audio(audio)
    return clip


def concatenate(phrase):
    clips = []
    u_uid = './users/' + str(uuid.uuid4())
    os.mkdir(u_uid)
    os.mkdir(u_uid + '/audio')
    for text in phrase.split(' '):
        get_img(text, u_uid)
        clips.append(create_vid(u_uid=u_uid, audio_path=create_audio(text, u_uid)))
    print(clips)
    concat_clip = concatenate_videoclips(clips, method="compose")
    concat_clip.write_videofile("test.mp4", fps=24)


if __name__ == '__main__':
    # create_vid('asfaf', create_audio('привет как твои дела?'))
    concatenate('как жить в россии дальше')
    # print(create_audio('привеет'))
