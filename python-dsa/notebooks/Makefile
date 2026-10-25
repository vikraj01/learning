.PHONY: start help install

start:           ## Open the notebooks in Jupyter (browser opens)
	uv sync
	uv run jupyter lab --notebook-dir=.

help:            ## Show this list
	@grep -E '^[a-z]+:.*##' $(MAKEFILE_LIST) | awk -F':.*## ' '{printf "  make %-8s %s\n", $$1, $$2}'

install:         ## Install Python and Jupyter (uses uv)
	uv sync
