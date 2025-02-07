.PHONY: all
all: lint test

.PHONY: lint
lint:
	ruff check src tests

.PHONY: test
test:
	pytest

.PHONY: format
format:
	black src tests
	#	yarn run prettier --write --trailing-comma es5 \
	#		*.js src/**/*.vue src/*/**.js

.PHONY: build
build:
	ruff check src tests
	yarn run build
	cp ./tailwind/dist/styles.css assets/css/
	alamano build

.PHONY: push
push:
	invoke deploy

.PHONY: deploy
deploy: push

.PHONY: clean
clean:
	rm -rf dist src/.temp

.PHONY: run
run:
	honcho start
