import io

import requests
from pprint import pprint


def searching(word):
    request_to_google = 'https://www.googleapis.com/customsearch/v1?cx=448c512f7ed8a5a3d&key=AIzaSyAI52k1NjCXVyJTnDuWAC1b94BCAnit7NQ&lr=lang_ru&searchType=image&q=' + word
    search_result = requests.get(request_to_google)
    list_links = [i['link'] for i in search_result.json()['items']]
    first_l = ''
    for i in list_links:
        if '.jpg' in i or '.jpeg' in i or '.JPG' in i:
            first_link = i
            break
    download_req = requests.get(first_link)
    return io.BytesIO(download_req.content)


# searching('Ярик')

def get_jpg(text):
    new_text = text.replace('  ', ' ')
    word = new_text.split(' ')
    return [searching(i) for i in word]


if __name__ == '__main__':
# get_jpg('Мишка косолапый По лесу идет, Шишки собирает, Песенки поет.')
