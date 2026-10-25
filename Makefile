.PHONY: help install serve build clean pdf labs notebooks

help:            ## Show this list
	@grep -E '^[a-z]+:.*##' $(MAKEFILE_LIST) | awk -F':.*## ' '{printf "  make %-10s %s\n", $$1, $$2}'

install:         ## Install MkDocs and Jupyter (uses uv)
	uv sync

serve: install   ## Open the notes at http://localhost:8000 (live reload)
	uv run mkdocs serve -a localhost:8000

build: install   ## Build the static site into site/
	uv run mkdocs build

clean:           ## Delete the built site
	rm -rf site

pdf: install     ## Build the two Python PDFs in python-dsa/ (needs google-chrome)
	uv run python python-dsa/pdf/build.py

notebooks: install ## Open the Python notebooks in Jupyter (browser opens)
	uv run jupyter lab --notebook-dir=python-dsa/notebooks

labs:            ## Open Docker Labs at http://localhost:7000 (installs and builds the first time)
	cd labs/app && npm install --no-audit --no-fund --silent && npm run build --silent && npm start
