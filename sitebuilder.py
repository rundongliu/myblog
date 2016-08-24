import sys
from flask import Flask, redirect, request, render_template, send_from_directory, url_for
from flask_flatpages import FlatPages
from flask_frozen import Freezer
from werkzeug import secure_filename
import os

DEBUG = True
FLATPAGES_AUTO_RELOAD = DEBUG
FLATPAGES_EXTENSION = '.md'
IMG_FOLDER = "img/"

app = Flask(__name__)
app.config.from_object(__name__)
flatpages = FlatPages(app)
pages = sorted([p for p in flatpages ], key=lambda item:item['date'], reverse=True)
freezer = Freezer(app)

@app.route('/')
def index():
    return render_template('index.html', pages=pages[:4])

@app.route('/allblogs/')
def show_blog():
    return render_template('allblog.html',  pages = pages)

@app.route('/blog/<path:path>/')
def page(path):
    page = flatpages.get_or_404(path)
    return render_template('post.html', page=page)
@app.route("/about/")
def about():
    return render_template('about.html')


@app.route("/img/<path:filename>/")
def blog_img(filename):
    path = os.path.join(app.root_path,"img")
    return send_from_directory(path, secure_filename(filename))

@freezer.register_generator
def img_url_generator():
    for filename in os.listdir(IMG_FOLDER):
        yield "/"+IMG_FOLDER+filename


if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == "build":
        freezer.freeze()
    else:
        app.run(port=8000)
