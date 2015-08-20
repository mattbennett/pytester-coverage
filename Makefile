coverage:
	coverage run -p -m pytest -s -v test --pdb && coverage combine && coverage report && rm .coverage

pytestcov:
	py.test --cov && rm .coverage
