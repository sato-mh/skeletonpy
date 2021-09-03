GOTOOLS = \
	github.com/uudashr/gopkgs/v2/cmd/gopkgs@latest \
	github.com/ramya-rao-a/go-outline@latest \
	github.com/cweill/gotests/gotests@latest \
	github.com/fatih/gomodifytags@latest \
	github.com/josharian/impl@latest \
	github.com/haya14busa/goplay/cmd/goplay@latest \
	github.com/go-delve/delve/cmd/dlv@latest \
	honnef.co/go/tools/cmd/staticcheck@latest \
	golang.org/x/tools/gopls@latest \
	golang.org/x/tools/cmd/goimports@latest \
	github.com/golangci/golangci-lint/cmd/golangci-lint@latest \

PYTOOLS = \
	pip \
	poetry \
	grpcio \
	grpcio-tools \
	grpclib \
	googleapis-common-protos \
	isort \
	flake8 \
	yapf \

PBTOOLS = \
	google.golang.org/protobuf/cmd/protoc-gen-go@latest \
	google.golang.org/grpc/cmd/protoc-gen-go-grpc@latest \
	github.com/grpc-ecosystem/grpc-gateway/v2/protoc-gen-grpc-gateway@latest \
	github.com/grpc-ecosystem/grpc-gateway/v2/protoc-gen-openapiv2@latest \
	github.com/bufbuild/buf/cmd/buf@latest \
	github.com/bufbuild/buf/cmd/protoc-gen-buf-breaking@latest \
	github.com/bufbuild/buf/cmd/protoc-gen-buf-lint@latest \
	github.com/fullstorydev/grpcurl/cmd/grpcurl@latest \

.PHONY: install
install: install-base install-golang install-python install-proto

.PHONY: install-base
install-base:
	@pip install -U poetry
	@poetry config virtualenvs.in-project true
	@poetry update

.PHONY: install-golang
install-golang:
	@for t in $(GOTOOLS); do echo "install $$t"; go install $$t; done

.PHONY: install-python
install-python:
	@for t in $(PYTOOLS); do echo "install $$t"; pip install -U $$t; done

.PHONY: install-proto
install-proto:
	@for t in $(PBTOOLS); do echo "install $$t"; go install $$t; done
