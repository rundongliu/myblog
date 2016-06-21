import sys
from flask import Flask, request, render_template, send_from_directory
from flask_flatpages import FlatPages
from flask_frozen import Freezer
from flask.ext.paginate import Pagination
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

PERPAGE=1

@app.route('/')
def index():
    return render_template('index.html', pages=pages)

@app.route('/allblogs/')
def show_blog():
    try:
        start_page = int(request.args.get('page', 1))
    except ValueError:
        start_page = 1
    #print start_page

    pagination = Pagination(page=start_page, total=len(pages), css_framework='bootstrap3', search=False, per_page=PERPAGE, record_name='blogs')
    return render_template('allblog.html',  pages = pages[start_page-1:start_page+PERPAGE-1], pagination=pagination)

    #return render_template('allblog.html',  pages = pages, pagination=pagination)

@app.route('/tag/<string:tag>/')
def tag(tag):
    tagged = [p for p in pages if tag in p.meta.get('tags', [])]
    return render_template('tag.html', pages=tagged, tag=tag)

@app.route('/blog/<path:path>/')
def page(path):
    page = flatpages.get_or_404(path)
    return render_template('post.html', page=page)
@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/sample")
def sample():
    return render_template('index.html')

@app.route("/contact")
def contact():
    return render_template('contact.html')

@app.route("/img/<path:filename>")
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
