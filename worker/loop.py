import asyncio
from engine.events import generate_events
from engine.predictor import predict
from websocket.manager import manager

async def run_loop():

    while True:

        events = generate_events()
        predictions = predict(events)

        await manager.broadcast({
            "events": events,
            "predictions": predictions
        })

        await asyncio.sleep(5)
