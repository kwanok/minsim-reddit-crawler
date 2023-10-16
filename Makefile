.PHONY: generate-post-proto
generate-post-proto:
	python -m grpc_tools.protoc -I ./src/grpc/post \
 		--python_out=./src/grpc/post --pyi_out=./src/grpc/post \
		--grpc_python_out=./src/grpc/post  \
		./src/grpc/post/post.proto

.PHONY: generate-comment-proto
generate-comment-proto:
	python -m grpc_tools.protoc -I ./src/grpc/comment \
 		--python_out=./src/grpc/comment --pyi_out=./src/grpc/comment \
		--grpc_python_out=./src/grpc/comment  \
		./src/grpc/comment/comment.proto

