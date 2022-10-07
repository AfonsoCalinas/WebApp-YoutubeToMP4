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
@app.route("/mp4/", methods=["POST", "GET"])
def mp4():
    if request.method == "POST":
        link = request.form["youtubeLink"]
        return redirect(url_for("showvideofirst", url=link))
    else:
        return render_template("mp4.html")

#SHOW VIDEO FIRST
@app.route("/showvideofirst/<url>/")
def showvideofirst(url):
    # link = request.args['youtubeLink']
    # yt = pytube.YouTube(link)
    # title = yt.title
    return render_template("showvideofirst.html", content=url)


@app.route("/<url>")
def youtubeURL(url):
    return f"<h1>{url}</h1>"

if __name__ == "__main__":
    app.run(debug=True)