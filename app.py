import socket
from os import environ

import requests
from flask import Flask

app = Flask(__name__)


@app.route("/health")
def health():
    return "OK"


@app.route("/")
def index():
    name = environ.get('NAME', 'Toby Qin')
    site = environ.get('SITE', 'https://tobyqin.github.io/docs')
    message = environ.get('MESSAGE', 'Kitty')
    color = environ.get('COLOR', 'aliceblue')
    image_url = environ.get('IMAGE', get_a_cat())
    host = socket.gethostname()

    return f"""
   <body style="background-color:{color};text-align:center;padding:20px;font-family: Verdana,sans-serif;">
   <div style="width:50%;margin:auto;box-shadow:0 10px 16px 0 rgba(0,0,0,0.2),0 6px 20px 0 rgba(0,0,0,0.19)">
    <img src="{image_url}" alt="{message}" style="width:100%">
      <div style="padding: 10px">
        <p>Hello {message}! <span style="color: gray" >Created by <a href="{site}">{name}</a> from {host}</span></p>
      </div>
    </div>
   </body>"""


def get_a_cat():
    return requests.get('https://api.thecatapi.com/v1/images/search').json()[0]['url']


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
