import sys, signal
import multiprocessing as mp
from time import time
from termcolor import colored as color

from checker import Checker
from datacompiler import DataCompiler


class Bruteman(object):
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





if __name__ == '__main__':
	main()



