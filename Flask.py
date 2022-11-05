import os
from urllib import response
from flask import Flask, jsonify, render_template, request
from flask import make_response
from index import main
from Controler.Transform import Transform

app = Flask(__name__)


@app.route("/<path:url>")
def default(url):
    return Transform.out(main(Transform.input(request, url)))


def get_qs(qs, key):
    try:
        id = qs[key]
    except KeyError:
        return False
    else:
        return id


# 启动服务，监听 9000 端口，监听地址为 0.0.0.0
app.run(port=9000, host='0.0.0.0')
