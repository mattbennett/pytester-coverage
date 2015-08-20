coverage_subproc:
	coverage run -p -m pytest -s -v test -k-pytest --pdb && coverage combine && coverage report && rm .coverage

coverage_pytest:
	coverage run -p -m pytest -s -v test -k-subproc --pdb && coverage combine && coverage report && rm .coverage

pytestcov_subproc:
	# doesn't work
	py.test --cov -k-pytest && rm .coverage

pytestcov_pytest:
	py.test --cov -k-subproc && rm .coverage
