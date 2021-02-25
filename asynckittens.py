#!/usr/bin/env python3





# import urllib.request
# #
# # print('Beginning file download with urllib2...')
# #
# # url = 'http://placekitten.com/300/300'
# urllib.request.urlretrieve(url, '/Users/RG/Projects/downloads/cat.jpg')

import random
import sys
import os
import urllib.request
import threading
from queue import Queue

from flask import Flask, request, send_from_directory, render_template


IMAGES = 4


class DownloadThread(threading.Thread):
    def __init__(self, queue, destfolder, number):
        super(DownloadThread, self).__init__()
        self.queue = queue
        self.destfolder = destfolder
        self.number = number
        self.daemon = True

    def run(self):
        while True:
            url = self.queue.get()
            try:
                self.download_url(url)
            except Exception as e:
                print("   Error: %s" % e)
            self.queue.task_done()

    def download_url(self, url):
        # change it to a different way if you require
        # name = url.split('/')[-1]
        name = "file_" + str(self.number)
        dest = os.path.join(self.destfolder, name)
        print("[%s] Downloading %s -> %s" % (self.ident, url, dest))
        urllib.request.urlretrieve(url, dest)


def download(urls, destfolder, numthreads=IMAGES):
    queue = Queue()
    for url in urls:
        queue.put(url)

    for i in range(numthreads):
        t = DownloadThread(queue, destfolder, i + 1)
        t.start()

    queue.join()


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


download(generate_urls(), "/Users/RG/Projects/static/images")


# set the project root directory as the static folder, you can set others.
app = Flask(__name__, static_url_path='')

@app.route('/js/<path:path>')
def send_js(path):
    return send_from_directory('js', path)

@app.route("/")
def main():
    return render_template('index.html')

# @app.route('/')
# def root():
#     return app.send_static_file('index.html')

if __name__ == "__main__":
    app.run()
