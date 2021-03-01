#!/usr/bin/env python3

import concurrent.futures
import random
import os
import urllib.request

from flask import Flask, request, redirect, url_for


IMAGES = 128


def get_size():
    return random.randint(200, 300)


def get_url():
    return "http://placekitten.com/" + str(get_size()) + "/" + str(get_size())


def generate_urls():
    urls = []
    for i in range(IMAGES):
        urls.append(get_url())
    print(len(urls))
    return urls


def download_url(url, number):
    name = "file_" + str(number)
    dest = os.path.join("/Users/RG/Projects/cognitive_space/async_downloads/python/static/images", name)
    print("Downloading %s -> %s" % (url, dest))
    urllib.request.urlretrieve(url, dest)


with concurrent.futures.ThreadPoolExecutor() as executor:
    futures = []
    for i in range(128):
        futures.append(executor.submit(download_url, url=get_url(), number=(i + 1)))
    for future in concurrent.futures.as_completed(futures):
        print(future.result())


# set the project root directory as the static folder, you can set others.
app = Flask(__name__, static_url_path='')


@app.route('/', methods=['GET'])
def metrics():
    return redirect(url_for('static', filename='index.html'))


if __name__ == "__main__":
    app.run()
