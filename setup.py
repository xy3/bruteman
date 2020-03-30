import setuptools

with open("README.md", "r") as fh:
	long_description = fh.read()


setuptools.setup(
	name="bruteman",
	version="0.0.1",
	author="XY3",
	author_email="a@xsq.pw",
	description="Bruteman login brute forcer",
	long_description=long_description,
	long_description_content_type="text/markdown",
	url="https://github.com/xy3/bruteman",
	packages=setuptools.find_packages(),
	classifiers=[
		"Programming Language :: Python :: 3",
		"License :: OSI Approved :: MIT License",
		"Operating System :: OS Independent",
	],
	python_requires='>=3.6',
	install_requires=[
		'requests',
		'json',
		'time',
		'pprint',
		'hashlib',
		'termcolor',
		'multiprocessing',
		'signal',
		'pyyaml'
	],
)