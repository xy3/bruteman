import yaml
from glob import glob

class ConfigParser(object):
	"""docstring for ConfigParser"""
	def __init__(self, filename=None):
		super(ConfigParser, self).__init__()
		if not filename:
			self.configfile = self.select_config()
		else:
			self.configfile = filename

		if not self.configfile:
			self.parsed = False
		else:
			self.loadconfig()
			self.parsed = True
	

	def select_config(self):
		configs = glob('configs/*.yml')
		lc = len(configs)
		
		if lc == 0:
			return False
		
		if lc == 1:
			choice = input(f"Do you want to use the config '{configs[0]}'? [Y/n]: ").lower()
			if choice in 'yY ':
				return configs[0]

		for i,c in enumerate(configs):
			print(f"{i:>{lc+1}}: {c}")
			choice = int(input(f"Enter the number of the config you wish to use: "))
			if lc >= choice:
				return configs[choice]

		return False


	def loadconfig(self):
		with open(self.configfile, 'r') as f:
			self.config = yaml.load(f.read())
