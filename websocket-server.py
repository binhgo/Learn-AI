import asyncio
import websockets
import json

USERS = set()


def users_event():
    return json.dumps({"type": "users", "count": len(USERS)})


def notify_users():
    if USERS:
        message = users_event()
        abc = [user.send(message) for user in USERS]
        await asyncio.wait(abc)


async def register(websocket):
    USERS.add(websocket)
    await notify_users()


async def unregister(websocket):
    USERS.remove(websocket)
    await notify_users()


async def hello(websocket, path):
    name = await websocket.recv()
    print(f"< {name}")

    greeting = f"Hello {name}!"

    await websocket.send(greeting)
    print(f"> {greeting}")


if __name__ == '__main__':
    print('wss server')

    start_server = websockets.serve(hello, "localhost", 8765)

    asyncio.get_event_loop().run_until_complete(start_server)
    asyncio.get_event_loop().run_forever()
