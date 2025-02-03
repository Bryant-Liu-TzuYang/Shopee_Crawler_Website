import os

from flask import (Flask, redirect, render_template, request,
                   send_from_directory, url_for)

from db import get_db

app = Flask(__name__)


@app.route('/')
def index():
    # Configure upload file path flask
    UPLOAD_FOLDER = 'uploads'
    OUTPUT_FOLDER = 'outputs'
    app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
    app.config['OUTPUT_FOLDER'] = OUTPUT_FOLDER
    files = list()
    db = get_db()

    db.execute(
        "INSERT INTO files (filename, status, stamp) VALUES (?, ?, ?)",
        ("aFilename", 'processing', "time_stamp")
    )

    return render_template('home_page.html', files=files)




import db
db.init_app(app)


if __name__ == '__main__':
   app.run()
