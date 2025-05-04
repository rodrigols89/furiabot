.PHONY: format lint check

# format the code (black and ruff).
format:
	black . --exclude environment
	ruff check . --fix --exclude environment

# linter the code (ruff).
lint:
	ruff check . --exclude environment

# Check the code (black and ruff).
check:
	black . --check --exclude environment
	ruff check . --exclude environment

addfuture:
	isort . --add-import 'from __future__ import annotations' --skip environment
