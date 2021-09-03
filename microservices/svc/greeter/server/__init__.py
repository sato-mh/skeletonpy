from grpclib.server import Server
from grpclib.utils import graceful_exit
from handler import Greeter


async def run(host: str = '0.0.0.0', port: int = 5050) -> None:
    server = Server([Greeter()])
    # Note: graceful_exit isn't supported in Windows
    with graceful_exit([server]):
        await server.start(host, port)
        print(f'Serving on {host}:{port}')
        await server.wait_closed()
