class DataCompiler(object):
	def __init__(self, pattern, data_format):
		self.pattern = pattern
		self.data_format = data_format


	def data(self, combo):
		self.email, self.password = combo.split(':', 1)

	def __str__(self):
		return f"{self.email}:{self.password} --> {json.dumps(self.data)}"
