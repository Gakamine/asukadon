import requests 
import sys
import random
import os
import os.path as op

from mastodon import Mastodon
from datetime import datetime

# --------------------------------------------------

DIR_SFW  = 'sfw/'
DIR_NSFW = 'nsfw/'

def main():

    mastodon = Mastodon(
        access_token = 'token.dat',
        api_base_url = 'https://antabaka.me/'
    )

    sfwcount  = len([name for name in os.listdir(DIR_SFW)  if os.path.isfile(os.path.join(DIR_SFW,  name))])
    nsfwcount = len([name for name in os.listdir(DIR_NSFW) if os.path.isfile(os.path.join(DIR_NSFW, name))])
    
    random_choice = random.randint(1, sfwcount + nsfwcount)
    print('\ns:' + str(sfwcount) + ' n:' + str(nsfwcount) + ' r:' + str(random_choice))
    
    is_safe = False if random_choice < nsfwcount else True
    art = ""
    
    if is_safe:
        files = [f for f in os.listdir(DIR_SFW) if op.isfile(op.join(DIR_SFW, f))]
        art = DIR_SFW  + random.choice(files)
    else:
        files = [f for f in os.listdir(DIR_NSFW) if op.isfile(op.join(DIR_NSFW, f))]
        art = DIR_NSFW + random.choice(files)

    fformat = op.splitext(art)[1][1:]
    if (fformat == 'jpg'):
        fformat = 'jpeg'

    with open(art, 'rb') as picture:
        data = picture.read()

    media = mastodon.media_post(data, f'image/{fformat}')
    toot  = f':gyate_reisen_love:'

    mastodon.status_post(toot, media_ids=[media], visibility='unlisted', sensitive=not is_safe)
    print(str(datetime.now()) + ': ' + art)

if __name__ == '__main__':
    sys.exit(main())
