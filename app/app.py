import os

from flask import (Flask, render_template,
                   request, jsonify, after_this_request, send_file)

from qr_code_generator import generate_qr_code


app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def index():
	if request.method == 'GET':
		return render_template("index.html")
	else:
		url = request.json['user_url']
		qr_code_file_name, qr_code_file_path = generate_qr_code(url)

		json_py_obj = {
			"qr_code_file_name": qr_code_file_name,
			"qr_code_file_path": qr_code_file_path,

		}
		response = jsonify(json_py_obj)
		response.headers.add('Access-Control-Allow-Origin', '*')
		return response


@app.route('/download/<file_name>', methods=['POST'])
def download_qr_code(file_name):
	file_path = os.path.join("static", "qr_codes", file_name)

	if os.path.exists(file_path):
		@after_this_request
		def remove_qr_code_file(response):
			os.remove(file_path)
			return response

		return send_file(file_path, download_rname=file_name,
			             as_attachment=True, max_age=0)
	else:
		return render_template("file_does_not_exist.html")


@app.errorhandler(403)
def bad_request_error_handler(error):
    return render_template("error_400.html")


@app.errorhandler(403)
def forbidden_error_handler(error):
    return render_template("error_403.html")


@app.errorhandler(404)
def page_not_found_error_handler(error):
    return render_template("error_404.html")


@app.errorhandler(500)
def server_error_hanlder(error):
    return render_template("error_500.html")


if __name__ == "__main__":
	app.run(debug=True)