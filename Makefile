
hello:
	echo "Hello" 
	echo "Hello"

build:
	python setup.py sdist bdist_wheel

install:
	pip3 install -e .