# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import comment_pb2 as comment__pb2
import grpc


class CommentStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.NewComment = channel.unary_unary(
                '/server.comment.Comment/NewComment',
                request_serializer=comment__pb2.NewCommentRequest.SerializeToString,
                response_deserializer=comment__pb2.NewCommentResponse.FromString,
                )


class CommentServicer(object):
    """Missing associated documentation comment in .proto file."""

    def NewComment(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_CommentServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'NewComment': grpc.unary_unary_rpc_method_handler(
                    servicer.NewComment,
                    request_deserializer=comment__pb2.NewCommentRequest.FromString,
                    response_serializer=comment__pb2.NewCommentResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'server.comment.Comment', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Comment(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def NewComment(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/server.comment.Comment/NewComment',
            comment__pb2.NewCommentRequest.SerializeToString,
            comment__pb2.NewCommentResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
