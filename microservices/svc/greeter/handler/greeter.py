from greeter.v1.greeter_grpc import GreeterBase
from greeter.v1.greeter_pb2 import HelloRequest, HelloResponse
from grpclib.server import Stream


class Greeter(GreeterBase):

    async def Hello(self, stream: Stream[HelloRequest, HelloResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        message = f'Hello, {request.name}!'
        await stream.send_message(HelloResponse(msg=message))
