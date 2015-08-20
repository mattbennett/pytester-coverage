coverage:
	coverage run -p --source app -m pytest -s -v test -k-pytest --pdb && coverage combine && coverage report && rm .coverage

experiment:
	coverage run -p --source app -m pytest -s -v test -k-subproc --pdb && coverage combine && coverage report && rm .coverage
