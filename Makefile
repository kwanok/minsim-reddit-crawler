.PHONY: generate-submission-proto
generate-submission-proto:
	python -m grpc_tools.protoc -I ./src/service/submission \
 		--python_out=./src/service/submission --pyi_out=./src/service/submission \
		--grpc_python_out=./src/service/submission  \
		./src/service/submission/submission.proto

.PHONY: generate-comment-proto
generate-comment-proto:
	python -m grpc_tools.protoc -I ./src/service/comment \
 		--python_out=./src/service/comment --pyi_out=./src/service/comment \
		--grpc_python_out=./src/service/comment  \
		./src/service/comment/comment.proto

.PHONY: image
image:
	docker build -t ghcr.io/kwanok/minsim-reddit-crawler:latest .

.PHONY: push
push:
	docker push ghcr.io/kwanok/minsim-reddit-crawler:latest

.PHONY: format
format:
	poetry run black .
	poetry run isort .
	poetry run ruff check . --fix

.PHONY: ci
ci: format image push

.PHONY: run
run:
	poetry run python -m src.main
