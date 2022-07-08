import pyautogui
import pyppeteer
import threading
import time

interval_sec = 1


def move_mouse():
	x, y = pyautogui.position()
	if x != y:
		pyautogui.moveTo(y, x)
	else:
		pyautogui.moveTo(y - 1, x)


def schedule():
	print('Interval run')
	move_mouse()
	return True


def run_program():
	print('Now Running')
	condition = True
	
	while condition:
		print('-')
		time.sleep(interval_sec)
		condition = schedule()


if __name__ == '__main__':
	run_program()
