import asyncio

import conf
import server

if __name__ == '__main__':
    asyncio.run(server.run(host=conf.IP_ADDRESS, port=conf.PORT))
