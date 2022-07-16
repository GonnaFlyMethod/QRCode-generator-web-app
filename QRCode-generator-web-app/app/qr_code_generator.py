import os

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

	file_name = f"qr_code_{date_today}_{hours}_{minutes}_{seconds}_{microseconds}.png"
	file_path = os.path.join("static", "qr_codes", file_name)

	img.save(file_path)
	return file_name, file_path

