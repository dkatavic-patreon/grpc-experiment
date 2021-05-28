# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import service.sidecar_pb2 as sidecar__pb2


class SideCarStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.getMessage = channel.unary_unary(
                '/SideCar/getMessage',
                request_serializer=sidecar__pb2.MessageConfig.SerializeToString,
                response_deserializer=sidecar__pb2.Message.FromString,
                )
        self.getMessageStream = channel.unary_stream(
                '/SideCar/getMessageStream',
                request_serializer=sidecar__pb2.MessageConfig.SerializeToString,
                response_deserializer=sidecar__pb2.Message.FromString,
                )
        self.ackMessage = channel.unary_unary(
                '/SideCar/ackMessage',
                request_serializer=sidecar__pb2.Message.SerializeToString,
                response_deserializer=sidecar__pb2.Empty.FromString,
                )


class SideCarServicer(object):
    """Missing associated documentation comment in .proto file."""

    def getMessage(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def getMessageStream(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ackMessage(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_SideCarServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'getMessage': grpc.unary_unary_rpc_method_handler(
                    servicer.getMessage,
                    request_deserializer=sidecar__pb2.MessageConfig.FromString,
                    response_serializer=sidecar__pb2.Message.SerializeToString,
            ),
            'getMessageStream': grpc.unary_stream_rpc_method_handler(
                    servicer.getMessageStream,
                    request_deserializer=sidecar__pb2.MessageConfig.FromString,
                    response_serializer=sidecar__pb2.Message.SerializeToString,
            ),
            'ackMessage': grpc.unary_unary_rpc_method_handler(
                    servicer.ackMessage,
                    request_deserializer=sidecar__pb2.Message.FromString,
                    response_serializer=sidecar__pb2.Empty.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'SideCar', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class SideCar(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def getMessage(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/SideCar/getMessage',
            sidecar__pb2.MessageConfig.SerializeToString,
            sidecar__pb2.Message.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def getMessageStream(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/SideCar/getMessageStream',
            sidecar__pb2.MessageConfig.SerializeToString,
            sidecar__pb2.Message.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ackMessage(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/SideCar/ackMessage',
            sidecar__pb2.Message.SerializeToString,
            sidecar__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)