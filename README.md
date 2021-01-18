# asuka-bot

Another bot for posting arts to your timeline. 

Currently posting on: https://antabaka.me/@asuka

This repo is a fork of https://dev.udongein.xyz/NaiJi/udonge-bot

### Initial setup

We support you to create a virtualenv to not pollute your system with modules:

```shell
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

Once it's done, you have to create a file `token.dat` in put in the account authorization's key. (no instruction given, it changes between your fediverse software).

Edit the `api_base_url` variable in `post-local.py` and `post-danbooru.py` sources. It must contain the url of the instance your bot is going to post on.

#### `post-local.py`

Allows you to post random arts from your local `/sfw` and `/nsfw` folder.

* Create `sfw` and `nsfw` folders in the same location with the `post-local.py` script.
* If you want to download a huge chunk of arts to your folder first, in `download.py` edit global variable `TAGS`, write in there 2 tags you need. Now run
```bash
python3 download.py
```
* In `post-local.py` edit `toot` variable, write in there a string you want the bot to write with any post. Hastags, for example.
* To make a single post, now run
```bash
python3 post-local.py
```

#### `post-danbooru.py`

Allows you to repost random arts from danbooru.donmai.us

* Edit `tags.dat` file. You can look at already defined tags and use it as example

```
#first line is for tags you want to search the arts with (must be exactly 2)
#second line is for tags you decline from posting completely (as many as you want)
#third line is for tags you want mastodon to mark as sensitive (as many as you want)
```
* To make a single post, now run
```bash
python3 post-danbooru.py
```
