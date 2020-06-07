test-unit: ## run unit tests
	poetry run pytest -vv -m "not integration"

test: ## run all tests
	poetry run pytest -vv --cov=src --cov-report term-missing

install-dev: ## install base and dev dependencies
	poetry install

lint: ## lint code
	poetry run black src tests --check --verbose 

fix-lint: ## lint code
	poetry run black src tests

upload-coverage: ## lint code
	codecov