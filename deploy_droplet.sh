#!/bin/bash

# - Create an Ubuntu 18.04 server.
# - Perform an `apt update` and `apt upgrade`.
# - Copy the `server.py` code to the server.
# - Start `server.py` code running: `python3 server.py`.
#
# You will be asked to run your script during your interview, wait for the setup, and then show resulting web page in your browser like: `http://your-server:8000`
#
# Note: you may have to spend a few cents to bring up the server. But then promptly delete the server once your done.
#
#
# ### server.py
#
# ```python
# import http.server
# import socketserver
# from http import HTTPStatus
#
#
# class Handler(http.server.SimpleHTTPRequestHandler):
#     def do_GET(self):
#         self.send_response(HTTPStatus.OK)
#         self.end_headers()
#         self.wfile.write(b'Hello world')
#
#
# httpd = socketserver.TCPServer(('', 8000), Handler)
# httpd.serve_forever()
# ```


doctl compute droplet create testdroplet --image ubuntu-18-04-x64 --size s-1vcpu-1gb --region nyc1

doctl compute ssh testdroplet


echo Hello World!
