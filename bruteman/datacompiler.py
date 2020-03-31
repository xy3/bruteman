import time
from hashlib import md5

class DataCompiler(object):
	def __init__(self, pattern, data_format):
		self.pattern = pattern
		self.data_format = data_format
		
		if ":" in pattern: self.delimiter = ":"
		elif "|" in pattern: self.delimiter = "|"
		elif ";" in pattern: self.delimiter = ";"
		
		self.splits = pattern.count(self.delimiter)
		self.variables = self.pattern.split(self.delimiter)


	def compile(self, combo):
		details = {}
		parts = combo.split(self.delimiter, self.splits)
		for i, p in enumerate(parts):
			details[self.variables[i]] = p

		data = {}		
		for k, v in self.data_format.items():
			# replace variable names with the value
			if v in details:
				data[k] = details[v]
			
			# replace time with timestamp
			elif v == 'time':
				data[k] = int(time.time())

			# Hash password if md5 in v
			elif 'md5' in str(v):
				pw = v.split()[1]
				if pw in details:
					data[k] = md5(details[pw].encode()).hexdigest()

			# TODO: add more hashing algorithms
			else:
				data[k] = v
		
		return data

