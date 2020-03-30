class User(object):
	def __init__(self, pattern):
		self.data = ''
		self.email, self.password = combo.split(':', 1)

	def __str__(self):
		return f"{self.email}:{self.password} --> {json.dumps(self.data)}"
