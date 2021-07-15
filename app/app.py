import os

from flask import (Flask, render_template,
                  request, send_file, after_this_request)

from qr_code_generator import generate_qr_code


app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def index():
	if request.method == 'GET':
		return render_template("index.html")
	else:
		url = request.form['content']
		qr_code_file_file_path = generate_qr_code(url)

		# @after_this_request
		# def remove_qr_code_file(response):
		# 	os.remove(qr_code_file_file_path)
		# 	return response

		return send_file(qr_code_file_file_path,
			             mimetype='image/PNG',
			             as_attachment=True)


@app.errorhandler(404)
def page_not_found(error):
    return 'This page does not exist', 404


if __name__ == "__main__":
	app.run(debug=True)