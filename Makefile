# Some simple testing tasks (sorry, UNIX only).

VENV=venv/bin
PYTHON=$(VENV)/python3
PIP=$(VENV)/pip


update:
	$(PIP) install -U .

env:
	test -d venv || python3 -m venv venv
	$(PIP) install -U pip

run:
	$(VENV)/jupyter notebook

remove-env:
	test -d venv && deactivate && rm -rf venv

force-env: remove-env env

install: env
	$(PIP) install -r requirements.txt

reinstall: force-env install

clean:
	rm -rf `find . -name __pycache__`
	rm -f `find . -type f -name '*.py[co]' `
	rm -f `find . -type f -name '*~' `
	rm -f `find . -type f -name '.*~' `
	rm -f `find . -type f -name '@*' `
	rm -f `find . -type f -name '#*#' `
	rm -f `find . -type f -name '*.orig' `
	rm -f `find . -type f -name '*.rej' `
	rm -f .coverage
	rm -rf coverage
	rm -rf build

