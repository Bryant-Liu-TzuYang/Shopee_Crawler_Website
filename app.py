import os
import pyodbc, struct
from azure import identity
from typing import Union
from pydantic import BaseModel

from flask import (Flask, redirect, render_template, request,
                   send_from_directory, url_for)


connection_string = os.environ["AZURE_SQL_CONNECTIONSTRING"]

app = Flask(__name__)


@app.route('/')
def index():
    # Configure upload file path flask
    UPLOAD_FOLDER = 'uploads'
    OUTPUT_FOLDER = 'outputs'
    app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
    app.config['OUTPUT_FOLDER'] = OUTPUT_FOLDER

    files = list()

    conn = get_conn()
    cursor = conn.cursor()

    cursor.execute("""
        IF NOT EXISTS (
        CREATE TABLE files (
            ID int NOT NULL PRIMARY KEY IDENTITY(1,1),
            filename NVARCHAR(255),
            status NVARCHAR(255),
            stamp TIMESTAMP
            )
        );
    """)

    conn.commit()

    return render_template('home_page.html', files=files)



def get_conn():
    credential = identity.DefaultAzureCredential(exclude_interactive_browser_credential=False)
    token_bytes = credential.get_token("https://database.windows.net/.default").token.encode("UTF-16-LE")
    token_struct = struct.pack(f'<I{len(token_bytes)}s', len(token_bytes), token_bytes)
    SQL_COPT_SS_ACCESS_TOKEN = 1256  # This connection option is defined by microsoft in msodbcsql.h
    conn = pyodbc.connect(connection_string, attrs_before={SQL_COPT_SS_ACCESS_TOKEN: token_struct})
    return conn


if __name__ == '__main__':
   app.run()



