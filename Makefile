.PHONY: test
test:
	flake8
	PYTHONPATH=src/ pytest tests/

.PHONY: run
run:
	pipenv run python3 src/server.py

.PHONY: install
	pipenv install