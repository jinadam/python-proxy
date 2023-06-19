from flask import Flask
from flask import request
import streamlit as st
import requests

app = Flask(__name__)


@app.route("/", defaults={"path": ""})
@app.route("/<string:path>")
@app.route("/<path:path>")
def proxy(path):  # put application's code here
    url = request.full_path
    method = request.method
    real_url = url[1:]
    if method == "POST":
        return requests.post(real_url, request.data)

    else:
        response = requests.get(real_url)
        return response.content, response.status_code, response.headers.items()


@app.route('/ping')
def ping():  # put application's code here
    url = request.host_url
    return url


@app.route('/streamlit')
def streamlit():
    st.set_page_config(page_title="My Streamlit App")
    st.write("Hello, world!")


if __name__ == '__main__':
    app.run()

if __name__ == '__main__':
    app.run()
