import argparse, sys
from bruteman import Bruteman
from configparser import ConfigParser
from pprint import pprint

def main():
	psr = argparse.ArgumentParser()
	psr.add_argument('-c', '--config', help="YAML Config file for Bruteman")
	psr.add_argument('logins', help="Login combinations file")
	args = psr.parse_args()

	cp = ConfigParser(args.config)
	
	if not cp.parsed:
		sys.exit(0)

	bm = Bruteman(cp.config)
	# pprint(cp.config)
	

if __name__ == '__main__':
	main()