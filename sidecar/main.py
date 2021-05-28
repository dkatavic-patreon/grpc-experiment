import grpc
from service import sidecar_pb2_grpc
from service import sidecar_pb2
from concurrent import futures
from time import sleep
import random
from enum import Enum



class Status(Enum):
    FETCHED = "fetched"
    PROCESSING = "PROCESSING"

class SQSMessage():
    i: int
    message: str
    status: Status

    def __init__(self, i, message):
        self.i = i
        self.message = message
        self.status = Status.FETCHED


def get_message_from_sqs(no_sleep=False):
    if not no_sleep:
        sleep(0.1)
    return SQSMessage(i=random.randint(0, 2**30), message="FooBar")


pool_of_messages = [get_message_from_sqs(no_sleep=True) for i in range(100)]
in_transit_messages = 0


def get_fetched_messages_in_memory():
    return [message for message in pool_of_messages if message.status is Status.FETCHED]


def get_message_for_processing_in_memory():
    message = get_fetched_messages_in_memory()[0]
    print(f"changing message {message.i} into {Status.PROCESSING.value}")
    message.status = Status.PROCESSING
    return message

def get_messages():
    while True:
        if len(get_fetched_messages_in_memory()) == 0:
            return
        else:
            yield get_message_for_processing_in_memory()



class SideCarServicer(sidecar_pb2_grpc.SideCarServicer):
    def getMessage(self, request, context):
        print("Returning getMessage")
        return sidecar_pb2.Message(id=1, text="Hello")

    def getMessageStream(self, request, context):
        print("getMessageStream invoked")
        print(f"in_transit_messages:{request.in_transit_messages}")
        global in_transit_messages
        in_transit_messages = request.in_transit_messages
        for message in get_messages():
            yield sidecar_pb2.Message(id=message.i, text=f"Hello: {message.message}")
            print(f"sent {message.i}")

    def ackMessage(self, request, context):
        print(f"ackMessage {request.id}")
        return sidecar_pb2.Empty()


def refresh_messages_from_sqs():
    """"Not used now"""
    while True:
        if len(get_fetched_messages_in_memory()) >= in_transit_messages * 2:
            print("Messages in memory are at limit, not pooling for SQS")
            sleep(5)
        else:
            print("Pooling for the new SQS message")
            message = get_message_from_sqs()
            message.status = Status.FETCHED
            pool_of_messages.append(message)




def serve():
    print("SERVING START")
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=1))
    sidecar_pb2_grpc.add_SideCarServicer_to_server(SideCarServicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()

    server.wait_for_termination()
    print("SERVING END")


if __name__ == '__main__':
    serve()
