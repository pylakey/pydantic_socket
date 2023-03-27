import asyncio
import logging

import pydantic

from pydantic_socket.types import Action
from pydantic_socket.websocket import Client

client = Client("http://127.0.0.1:8080", auto_reconnect=False, client_id=1)


class SomeActionInputPayload(pydantic.BaseModel):
    input: str


async def main():
    # Establishing connection to server
    asyncio.create_task(client.run())
    # Wait some time until connection is done
    await asyncio.sleep(2)
    # Send action
    await client.send(Action(type='hello', payload={"name": "pydantic_socket"}))
    # Send and wait for response
    response = await client.request(Action(type='test', payload={"input": "Some Input"}))
    logging.info(f"Payload is: {response.payload}")
    await client.close()


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
