#!/usr/bin/python3.6

import os
import uuid
import sqlite3
from flask import Flask, request, jsonify, send_from_directory
from werkzeug.utils import secure_filename
from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app)

app.config.from_object(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'

conn = sqlite3.connect('db.sqlite')
c = conn.cursor()


# FIXME: Flask in debug mode runs the code here two times, because reasons (?)

try:
	c.execute('SELECT COUNT(id) FROM files')
	print(c.fetchone()[0], 'uploads in database')
except:
	c.execute("""
	         	CREATE TABLE `files` (
						`id`	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
						`uploadUUID`	TEXT NOT NULL,
						`folderPath`	TEXT NOT NULL,
						`fileName`	TEXT NOT NULL
					);
	          """)
	print('Initialized database')
conn.commit()
conn.close()

# TODO: serve the production build of the Vue app during development
#  (define environments)

print("test")

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
			conn = sqlite3.connect('db.sqlite')
			c = conn.cursor()
			filename = secure_filename(file.filename)
			uploadID = uuid.uuid4().hex[0:9]
			folderPath = app.config['UPLOAD_FOLDER']+'/'+ uploadID
			os.makedirs(folderPath)
			file.save(os.path.join(app.config['UPLOAD_FOLDER'], uploadID, filename))
			c.execute("""
			          INSERT INTO `files` (`uploadUUID`, `folderPath`, `fileName`) VALUES (
			          	?,?,?) 
			          """, (uploadID,folderPath,filename,))
			conn.commit()
			conn.close()
			response = jsonify({'uploadUUID': uploadID})
			return response

# FIXME: Flask as production server to serve files? :thinking:
@app.route('/file/<fileID>', methods=['GET'])
def serve_file(fileID):
	print(fileID)
	conn = sqlite3.connect('db.sqlite')
	c = conn.cursor()
	#return send_from_directory(folder, name, as_attachment=True)
	return 400
	conn.commit()
	conn.close()
	

if __name__ == "__main__":
	app.run(debug=True)