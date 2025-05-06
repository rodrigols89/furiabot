.PHONY: format check

# format the code (black and ruff).
format:
	isort . --add-import 'from __future__ import annotations' --skip environment
	isort . --profile black --skip environment
	black . --exclude environment
	ruff check . --fix --exclude environment

# Check the code (black and ruff).
check:
	black . --check --exclude environment
	ruff check . --exclude environment
