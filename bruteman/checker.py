import requests, json, sys
from pprint import pprint
from termcolor import colored as color



class Checker(object):
	def __init__(self, config):
		self.url = config['url']
		self.method = config['method']
		self.success_keyword = config['success_keyword']
		self.session = requests.Session()
		self.session.headers.update(config['headers'])



	def check(self, data, combo, queue):
		try:
			if self.method == 'post':
				res = self.session.post(self.url, data)
			else:
				res = self.session.get(self.url, data)
		except Exception as e:
			queue.put('bad')
			return
		
		if res.status_code == 200:
			content = res.text
			# if config['response_type'] == 'json':
				# content = json.loads(res.content)
			
			if self.success_keyword in content:
				queue.put(combo)
				return combo
			
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



