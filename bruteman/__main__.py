import argparse
# from .bruteman import Bruteman


def main():
	psr = argparse.ArgumentParser()
	psr.add_argument('-c', '--config', help="YAML Config file for Bruteman", required=True)
	psr.add_argument('-l', '--logins', help="Login combinations file", required=True)
	args = psr.parse_args()

	

if __name__ == '__main__':
	main()