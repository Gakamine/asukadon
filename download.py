import requests 
import sys

import os.path as op

TAGS = 'souryuu_asuka_langley'

def main():

    PAGE = 0
    rejected_once = False

    while True:

        URL    = "https://safebooru.donmai.us/posts.json"
        PARAMS = { 'tags': TAGS,
                   'page': PAGE } 

        r = requests.get(url = URL, params = PARAMS) 
        data = r.json()

        # If didn't receive a single entity, we should try again.
        # If failed another time, shutdown!
        if data.count == 0:
            if rejected_once == True:
                return
            rejected_once = True
            continue
        rejected_once = False

        for entity in data:
            file_tags = entity['tag_string']

            # we don't want comics
            if 'comic' in file_tags:
                continue

            try:
                file_url = entity['file_url']
            except:
                continue

            # write the art
            img_data = requests.get(file_url).content
            with open('source/' + file_url[file_url.rfind("/")+1:], 'wb') as handler:
                handler.write(img_data)
            
            # save its url separately into a file
            with open('urls', 'a', encoding='utf-8') as file:
                print(file_url, file=file)

        PAGE += 1

    # end while True

if __name__ == '__main__':
    sys.exit(main())
