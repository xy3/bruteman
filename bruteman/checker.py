import requests, json, sys
from time import time
from pprint import pprint
from hashlib import md5
from termcolor import colored as color
import multiprocessing as mp
import signal
import yaml



class Checker(object):
	def __init__(self, url, headers):
		self.url = url
		self.session = requests.Session()
		self.session.headers.update(headers)



	def check(self, data, queue):
		try:
			res = self.session.post(URL, data)
		except Exception as e:
			queue.put('bad')
			return
		

		if res.status_code == 200:
			# content = json.loads(res.content)
			# if content['AccessToken'] != '':
			# 	user.data = content
				queue.put(user)
				return user
			
		queue.put('bad')
		return False



	def listener(self, queue):
		# listens for messages on the queue, writes to good.txt 
		good = 0
		bad = 0
		with open('good.txt', 'a+') as f:
			while 1:
				m = queue.get()
				if m == 'kill':
					break
				if m == 'bad':
					bad += 1
				else:
					good += 1
					f.write(str(m) + '\n')
				f.flush()

				print(color(" Good:", 'green'), good, color("Bad:", 'red'), bad, end='\r')

		print(color(" Good:", 'green'), good, color("Bad:", 'red'), bad)



