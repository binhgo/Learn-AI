import asyncio
import websockets



def abc():
    asyncio.wait([user.send(message) for user in USERS])


async def client_hello():
    uri = "ws://localhost:8765"
    async with websockets.connect(uri) as websocket:
        name = input("What's your name? ")

        await websocket.send(name)
        print(f"> {name}")

        greeting = await websocket.recv()
        print(f"< {greeting}")


if __name__ == '__main__':
    print('wss client')
    asyncio.get_event_loop().run_until_complete(client_hello())
    asyncio.wait()
