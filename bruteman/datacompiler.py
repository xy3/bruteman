class DataCompiler(object):
	def __init__(self, pattern, data_format):
		self.pattern = pattern
		self.data_format = data_format
		
		if ":" in pattern: self.delimiter = ":"
		elif "|" in pattern: self.delimiter = "|"
		elif ";" in pattern: self.delimiter = ";"
		
		self.splits = pattern.count(self.delimiter)
		self.variables = self.pattern.split(self.delimiter)

		# for k,v in data_format:
			# if v in self.variables


	def compile(self, combo):
		details = {}
		parts = combo.split(self.delimiter, self.splits)
		for i, p in enumerate(parts):
			details[self.variables[i]] = p

		data = {}		
		for k, v in self.data_format.items():
			if v in details:
				# if v is a variable name, replace it
				# with the value into data_format
				data[k] = details[v]
		
		return data

