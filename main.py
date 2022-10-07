from flask import Flask, redirect, url_for, render_template, request
import pytube
import ffmpeg
import os

app = Flask(__name__)

SAVE_PATH = "C:\\Users\\calin\\Desktop\\test"

# INDEX
@app.route("/")
def index():
        return render_template("index.html")

# MP4
@app.route("/mp4/")
def mp4():
    return render_template("mp4.html")

#SHOW VIDEO FIRST
@app.route("/mp4/showvideofirst/")
def showvideofirst():
    # link = request.args['youtubeLink']
    # yt = pytube.YouTube(link)
    # title = yt.title
    return render_template("showvideofirst.html")


@app.route("/<url>")
def youtubeURL(url):
    return f"<h1>{url}</h1>"

if __name__ == "__main__":
    app.run(debug=True)