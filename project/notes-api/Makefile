.PHONY: check fix test

check:
	ruff check .
	black --check .
	pytest

fix:
	ruff check --fix .
	black .

test:
	pytest
