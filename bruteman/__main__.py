import requests, json, sys
from time import time
from pprint import pprint
from hashlib import md5
from termcolor import colored as color
import multiprocessing as mp
import signal
import yaml


def main():
	bm = Checker()
	bm.setheaders()
	
	pool = mp.Pool(60, init_worker)
	manager = mp.Manager()
	queue = manager.Queue()
	
	# Listener to write working combos to file
	pool.apply_async(bm.listener, (queue,))
	
	starting_index = 0
	inp = input("Starting index (0): ").strip()
	if len(inp):
		starting_index = int(inp)
	

	jobs = []
	i = -1
	total_lines = 0

	try:
		with open(sys.argv[1], 'r') as combo_file:
			for combo in combo_file:
				i += 1
				total_lines += 1
				
				if i < starting_index:
					continue
				
				combo = combo.strip()
				if ':' in combo:
					user = User(combo)
					job = pool.apply_async(bm.check, (user, queue))
					jobs.append(job)
		
		print(color('Total to check: ', 'cyan'), total_lines - starting_index)

		# Run the jobs
		for job in jobs: 
			job.get()

		# Kill the listener
		queue.put('kill')
		pool.close()
		pool.join()


	except KeyboardInterrupt as e:
		queue.put('kill')
		pool.terminate()
		pool.join()
		sys.exit()
	


if __name__ == '__main__':
	main()



def init_worker():
	signal.signal(signal.SIGINT, signal.SIG_IGN)

