lint:
	flake8 perfi tests

test:
	py.test tests --cov=perfi --cov-report term-missing --cov-branch

install:
	pip install -e .
