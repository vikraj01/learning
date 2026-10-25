.PHONY: help start install build dev typecheck clean reset-progress

APP := app

help:            ## Show this list
	@grep -E '^[a-z-]+:.*##' $(MAKEFILE_LIST) | awk -F':.*## ' '{printf "  make %-15s %s\n", $$1, $$2}'

start: build     ## Open Docker Labs at http://localhost:7000
	cd $(APP) && npm start

install:         ## Install the app's packages
	cd $(APP) && npm install --no-audit --no-fund --silent

build: install   ## Build the site into app/dist
	cd $(APP) && npm run build --silent

dev: install     ## Live-reload mode: site on :5173, server on :7000
	cd $(APP) && npm run dev

typecheck: install ## Check the TypeScript
	cd $(APP) && npm run typecheck

clean:           ## Remove the built site and installed packages
	rm -rf $(APP)/dist $(APP)/node_modules

reset-progress:  ## Forget solved labs and delete every lab workspace
	rm -rf workspace .progress.json
