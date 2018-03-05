#!/usr/bin/python3.6

import os
from flask import Flask, request
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.config.from_object(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'

@app.route('/upload', methods=['POST'])
def upload_file():
	if request.method == 'POST':
		if 'file' not in request.files:
			return 400, 'Bad request'
		if file.filename == '':
			return 400, 'Bad request'
		if file:
			filename = secure_filename(file.filename)
			file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
			return 200, 'Success'

if __name__ == "__main__":
	app.run(debug=True)