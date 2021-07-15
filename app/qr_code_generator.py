from datetime import datetime, date

import qrcode


def generate_qr_code(url: str) -> str:
	img = qrcode.make(url)

	timestamp = datetime.now()

	date_today = date.today().strftime("%d_%m_%Y")

	hours = timestamp.hour
	minutes = timestamp.minute
	seconds = timestamp.second
	microseconds = timestamp.microsecond

	file_path = f"qr_codes/qr_code_{date_today}_{hours}_{minutes}_{seconds}_{microseconds}"
	#file_object = io.BytesIO()
	#img.save(file_object, 'PNG')

	# Move to beginning of file so `send_file()` it will read from start
	#file_object.seek(0)
	img.save(file_path)

	return file_path

