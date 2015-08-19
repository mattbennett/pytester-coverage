coverage:
	coverage run -p --source app -m pytest -s -v test && coverage combine && coverage report && rm .coverage
