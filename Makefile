.PHONY: all
all: start

.PHONY: start
start:
	. ./tools/setup.sh

.PHONY: validate
validate: lint test

.PHONY: lint
lint:
	@echo "Linting via PEP8"
	pep8 --exclude=migrations,venv,.git

.PHONY: test
test:
	@echo "Testing"
	python manage.py test

.PHONY: pip
pip:
	pip install -r requirements.txt

.PHONY: dev
dev:
	python manage.py runserver 3000
