from fastapi import FastAPI, WebSocket
import asyncio

from worker.loop import run_loop
from websocket.manager import manager

app = FastAPI()

@app.on_event("startup")
async def startup():
    asyncio.create_task(run_loop())

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await manager.connect(websocket)

    while True:
        await websocket.receive_text()
