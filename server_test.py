import asyncio
import logging

import pydantic_socket
from pydantic_socket.types import Action
from pydantic_socket.websocket import (
    Server,
    ServerClient,
)

server = Server()


class TestResponse(pydantic_socket.types.BaseModel):
    foo: int = 1
    bar: str = "bar"
    input: str | None = None


@server.action_handler("hello")
async def hello_handler(s: Server, client: ServerClient, action: Action):
    logging.info(f"Hello, {action.payload.get('name', 'World')}!")


async def test_handler(s: Server, client: ServerClient, action: Action):
    return TestResponse(foo=1, bar="bar", input=action.payload.get('input'))


server.set_action_handler("test", test_handler)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.run(server.run())
