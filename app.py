#!/usr/bin/python3.6

import os
import uuid
import sqlite3
from flask import Flask, request, jsonify
from werkzeug.utils import secure_filename
from flask_cors import CORS, cross_origin


app = Flask(__name__)
CORS(app)

app.config.from_object(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'

conn = sqlite3.connect('db.sqlite')

@app.route('/upload', methods=['POST'])
def upload_file():
	print(request)
	if request.method == 'POST':
		if 'file' not in request.files:
			return 'Bad request', 400
		file = request.files['file']
		if file.filename == '':
			return 'Bad request', 400
		if file:
			filename = secure_filename(file.filename)
			uploadID = uuid.uuid4().hex[0:6]
			os.makedirs(app.config['UPLOAD_FOLDER']+'/'+ uploadID)
			file.save(os.path.join(app.config['UPLOAD_FOLDER'], uploadID, filename))
			response = jsonify({'uploadUUID': uploadID})
			return response

if __name__ == "__main__":
	app.run(debug=True)