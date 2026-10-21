.PHONY: help install serve build clean

help:            ## Show this list
	@grep -E '^[a-z]+:.*##' $(MAKEFILE_LIST) | awk -F':.*## ' '{printf "  make %-8s %s\n", $$1, $$2}'

install:         ## Install MkDocs (uses uv)
	uv sync

serve: install   ## Open the notes at http://localhost:8000 (live reload)
	uv run mkdocs serve -a localhost:8000

build: install   ## Build the static site into site/
	uv run mkdocs build

clean:           ## Delete the built site
	rm -rf site
