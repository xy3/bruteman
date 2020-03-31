import sys, signal, argparse
import multiprocessing as mp
from time import time
from termcolor import colored as color
from pprint import pprint


from configparser import ConfigParser
from checker import Checker
from datacompiler import DataCompiler


class Bruteman(object):
	"""docstring for Bruteman"""
	def __init__(self, config, combos):
		self.combos = combos
		self.checker = Checker(config)
		
		self.pool = mp.Pool(config['threads'], self.init_worker)
		self.queue = mp.Manager().Queue()
		self.dc = DataCompiler(config['pattern'], config['data_format'])

	
	def init_worker(self):
		signal.signal(signal.SIGINT, signal.SIG_IGN)

	
	def start(self):
		# Listener to write working combos to file
		self.pool.apply_async(self.checker.listener, (self.queue,))
		
		starting_index = 0
		inp = input("Starting index (0): ").strip()
		if len(inp):
			starting_index = int(inp)
		

		jobs = []
		i = -1
		total_lines = 0

		try:
			with open(self.combos, 'r') as combo_file:
				for combo in combo_file:
					i += 1
					total_lines += 1
					
					if i < starting_index:
						continue
					
					combo = combo.strip()

					data = self.dc.compile(combo)
					
					if data:
						job = self.pool.apply_async(self.checker.check, (data, combo, self.queue))
						jobs.append(job)
			
			print(color('Total to check: ', 'cyan'), total_lines - starting_index)

			# Run the jobs
			for job in jobs: 
				job.get()

			self.quit()

		except KeyboardInterrupt as e:
			self.quit()
			sys.exit()


	def quit(self):
		self.queue.put('kill') # Kill the listener
		self.pool.terminate()
		self.pool.join()




def main():
	psr = argparse.ArgumentParser()
	psr.add_argument('-c', '--config', help="YAML Config file for Bruteman")
	# TODO: directory change in code
	psr.add_argument('-o', '--output', metavar='OUTPUT DIR', help="Output directory to save working and failed combinations")
	
	psr.add_argument('combos', help="Login combinations file")
	args = psr.parse_args()

	cp = ConfigParser(args.config)
	
	if not cp.parsed:
		sys.exit(0)

	bm = Bruteman(cp.config, args.combos)
	bm.start()
	

if __name__ == '__main__':
	main()



