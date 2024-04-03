from flask import Flask, render_template, url_for, request
import requests
import os.path as op


directory = op.dirname(__file__)

app = Flask("proxy-segmonto", template_folder=f"{directory}/templates")

@app.route("/")
def main():
    return render_template("index.html")

@app.route("/proxy")
def proxy():
    uri = request.args.get("uri")
    if not uri:
        return 404, "Missing URI"
    resp = requests.get(uri, headers={"Authorization": request.headers.get("Authorization", ""), "Application": "LiveSegmonto"})
    return resp.content