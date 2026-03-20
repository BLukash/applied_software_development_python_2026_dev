.PHONY: check fix test

check:
	uv run ruff check .
	uv run black --check .
	uv run pytest

fix:
	uv run ruff check --fix .
	uv run black .

test:
	uv run pytest
