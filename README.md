# gRPC POC

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