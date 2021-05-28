# gRPC POC

## Install dependencies

```bash
pip install -r requirements.txt
```

## Generate Stub and Servicer

From root directory run
```bash
python -m grpc_tools.protoc --python_out=./service/ --grpc_python_out=./service/ --proto_path=./service/  sidecar.proto
```
Then fix import in `service/sidecar_pb2_grpc.py` 
```python
# From
import sidecar_pb2 as sidecar__pb2
# To
import service.sidecar_pb2 as sidecar__pb2
```
generator is probably missused which results in broken imports, that needs to be fixed

## Start Servicer

```bash
python ./sidecar/main.py 
```

Servicer will stream messages to the client. You can play around with the settings, like number of messages

## Start Client/Service (Like tax service)

```bash
python ./service/main.py 
```

Client consumes messages with fixed 100ms delay, which will emulate backpressure. You can play around with the settings in the code

## Result of the experiment

Goal is to evaluate using gRPC for communication between sidecar and service. Main features tested is gRPC flow-control using streams

gRPC builds on top of HTTP/2. gRPC flow-control in streaming data to client leverages HTTP/2 flow-control [link to the specs
](https://httpwg.org/specs/rfc7540.html#FlowControl) . ```Flow control is directional with overall control provided by the receiver. A receiver MAY choose to set any window size that it desires for each stream and for the entire connection. A sender MUST respect flow-control limits imposed by a receiver. Clients, servers, and intermediaries all independently advertise their flow-control window as a receiver and abide by the flow-control limits set by their peer when sending.```

This will help gRPC automatically handle backpressure, but the problem is that we have lose controls about number of messages in transit. This could work great for pub/sub pattern, but the problem with the queue workers is that the message could be stuck in the client backlog (message sent from sidecar to service, but service has still not started processing it) for a long time and we don't have a lot of control over it. If we scale number of workers, we wouldn't be able to send the message to the new worker, which could be especially problematic with priority queues 