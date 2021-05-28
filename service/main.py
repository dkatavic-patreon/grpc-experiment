import grpc
from service import sidecar_pb2_grpc
from service import sidecar_pb2
from concurrent import futures
from time import sleep

def get_message(stub):
    message = stub.getMessage(sidecar_pb2.MessageConfig())
    print("message:")
    print(message)


def ack_message(stub, message):
    print(f"ack_message: {message.id}")
    stub.ackMessage(sidecar_pb2.Message(
        id=message.id,
        text=message.text
    ))

def get_message_stream(stub):
    print("get_message_stream")
    for message in stub.getMessageStream(sidecar_pb2.MessageConfig(
            in_transit_messages= 10
    )):
        print(message)

        sleep(0.1)
        # ack_message(stub, message)


def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = sidecar_pb2_grpc.SideCarStub(channel)
        # get_message(stub)
        ack_message(stub, sidecar_pb2.Message(id=1))
        ack_message(stub, sidecar_pb2.Message(id=1))
        ack_message(stub, sidecar_pb2.Message(id=1))
        get_message_stream(stub)


if __name__ == "__main__":
    run()