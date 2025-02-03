import os

from flask import (Flask, redirect, render_template, request,
                   send_from_directory, url_for)

app = Flask(__name__)


@app.route('/')
def index():
   files = list()
   return render_template('home_page.html', files=files)


import db
db.init_app(app)


if __name__ == '__main__':
   app.run()
