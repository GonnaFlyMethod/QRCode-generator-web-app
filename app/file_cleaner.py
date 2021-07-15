import time
import os


def delete_file(delay_in_minutes, file_path):
	time_seconds = 60 * delay_in_minutes

	time.sleep(time_seconds)

	try:
		os.remove(file_path)
	except FileNotFoundError:
		pass