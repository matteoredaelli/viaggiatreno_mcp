.PHONY: help run pytest ruff-format ruff-check pyright lint build publish

# Default goal
help:
	@echo "Usage: make <target>"
	@echo ""
	@echo "Targets:"
	@echo "  help          Show this help (default)"
	@echo "  run           Run the MCP server (uv run)"
	@echo "  pytest        Run tests with pytest"
	@echo "  ruff-format   Format code with ruff"
	@echo "  ruff-check    Lint code with ruff (with --fix on demand via FIX=1)"
	@echo "  pyright       Run type checking with pyright"
	@echo "  lint          ruff-format --check + ruff-check + pyright"
	@echo "  build         Build sdist and wheel with uv"
	@echo "  publish       Build and publish to PyPI (needs UV_PUBLISH_TOKEN)"
	@echo "  lint          ruff-format --check + ruff-check + pyright"

addlicense:
	$$HOME/go/bin/addlicense -c "Matteo Redaelli" -l GPL-3.0-or-later  -s  ./**/*.py

run:
	uv run viaggiatreno-mcp

pytest:
	uv run pytest

ruff-format:
	uv run ruff format .

ruff-check:
ifdef FIX
	uv run ruff check --fix .
else
	uv run ruff check .
endif

pyright:
	uv run pyright

lint: ruff-format ruff-check pyright

build:
	uv build

publish: build
	uv publish
