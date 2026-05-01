class ConnectionManager:

    def __init__(self):
        self.clients = []

    async def connect(self, websocket):
        await websocket.accept()
        self.clients.append(websocket)

    async def broadcast(self, message):

        for client in self.clients:
            await client.send_json(message)

manager = ConnectionManager()
