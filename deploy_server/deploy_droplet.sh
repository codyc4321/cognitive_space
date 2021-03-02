#!/bin/bash

# - Create an Ubuntu 18.04 server.
# - Perform an `apt update` and `apt upgrade`.
# - Copy the `server.py` code to the server.
# - Start `server.py` code running: `python3 server.py`.
#
# You will be asked to run your script during your interview, wait for the setup, and then show resulting web page in your browser like: `http://your-server:8000`
#
# Note: you may have to spend a few cents to bring up the server. But then promptly delete the server once your done.

# doctl auth init
#
# doctl compute ssh testdroplet
#
# doctl compute droplet create testdroplet --image ubuntu-18-04-x64 --size s-1vcpu-1gb --region nyc1

doctl compute ssh testdroplet --ssh-command 'apt update'

doctl compute ssh testdroplet --ssh-command 'apt upgrade'

doctl compute ssh testdroplet --ssh-command 'mkdir web'

doctl compute ssh testdroplet --ssh-command 'touch ./web/server.py'

doctl compute ssh testdroplet --ssh-command 'echo -e "import http.server\nimport socketserver\nfrom http import HTTPStatus\n\nclass Handler(http.server.SimpleHTTPRequestHandler):\n    def do_GET(self):\n        self.send_response(HTTPStatus.OK)\n        self.end_headers()\n" >> web/server.py'
doctl compute ssh testdroplet --ssh-command "printf '        self.wfile.write(b' >> web/server.py"
doctl compute ssh testdroplet --ssh-command "printf \' >> web/server.py"
doctl compute ssh testdroplet --ssh-command "printf 'Hello world' >> web/server.py"
doctl compute ssh testdroplet --ssh-command "printf \' >> web/server.py"
doctl compute ssh testdroplet --ssh-command "printf ')\n\n\n' >> web/server.py"
doctl compute ssh testdroplet --ssh-command "printf 'httpd = socketserver.TCPServer((' >> web/server.py"
doctl compute ssh testdroplet --ssh-command "printf \' >> web/server.py"
doctl compute ssh testdroplet --ssh-command "printf \' >> web/server.py"
doctl compute ssh testdroplet --ssh-command "printf ', 8000), Handler)\nhttpd.serve_forever()' >> web/server.py"

doctl compute ssh testdroplet --ssh-command 'python3 web/server.py'
