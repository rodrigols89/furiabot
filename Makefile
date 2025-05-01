.PHONY: format lint check

# format the code (black and ruff).
format:
	black .
	ruff check . --fix

# linter the code (ruff).
lint:
	ruff check .

# Check the code (black and ruff).
check:
	black . --check
	ruff check .
