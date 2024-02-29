# Self-Documented Makefile see https://marmelab.com/blog/2016/02/29/auto-documented-makefile.html

.DEFAULT_GOAL := help

create-env: ## Create python virtual env
	python -m venv .env && source .env/bin/activate && pip install --upgrade pip

poetry-install: create-env ## Create and install environment for local dev
	  source .env/bin/activate && poetry install

install-hooks: ## Install hooks
	source .env/bin/activate && pre-commit install

clean-hooks: ## Clean hooks
	pre-commit clean

setup-local-dev: poetry-install install-hooks ## Setup the local environment

test: ## Run pytest with coverage and html report
	poetry run pytest . -vv -p no:warnings --cov=. --cov-report=xml --cov-report=html

test-local: ## Run pytest with coverage without generating the report
	poetry run pytest . -vv -p no:warnings --cov=.

fmt: ## Run ruff formatter in all files under src
	poetry run ruff format src

lint:  ## Run ruff linter in all files under src
	poetry run ruff check src

check:  ## Run ruff lint,formatter,isort in all files under src
	poetry run ruff src

clean:  ## Delete temp dirs
	rm -rf  .pytest_cache coverage.xml .mypy_cache  .coverage .coverage.* htmlcov


.PHONY: help create-env poetry-install install-hooks clean-hooks setup-local-dev \
   		test test-local fmt lint \
 		check clean


help:
	@awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z_-]+:.*?## / {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}' $(MAKEFILE_LIST)