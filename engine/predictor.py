from core.cache import CACHE

def predict(events):

    predictions = []

    for e in events:

        if e["type"] == "FX_STRESS":
            predictions.append({
                "forecast": "CURRENCY_VOLATILITY",
                "confidence": 0.7
            })

    CACHE["predictions"] = predictions
    return predictions
