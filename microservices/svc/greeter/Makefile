.PHONY: all
all: pre fmt lint

.PHONY: pre
pre:
	@poetry update

.PHONY: fmt
fmt:
	@yapf -r -i --exclude .git .
	@isort .

.PHONY: lint
lint:
	@flake8
