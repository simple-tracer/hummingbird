from flask import Flask, request, redirect, url_for, render_template

from airtable import Airtable

from dotenv import load_dotenv

import os

import urllib

from urllib.request import urlopen, Request

import ast

import json

from datetime import datetime

load_dotenv()

app = Flask(__name__)


places_table = Airtable(os.getenv("AIRTABLE_BASE"),
                       'Places', os.getenv("AIRTABLE_KEY"))


@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')

@app.route('/create', methods=['POST'])
def create():
    record = places_table.insert({"Place Name": str(request.form['place-name']),})

    return render_template('done.html', id=record['id'])


if __name__ == '__main__':
    from os import environ
    app.run(debug=False, host='0.0.0.0', port=environ.get("PORT", 5000))
