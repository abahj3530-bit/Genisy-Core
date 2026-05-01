from core.cache import CACHE

def generate_events():

    events = [
        {"type": "FX_STRESS", "severity": "MEDIUM"},
        {"type": "VESSEL_ACTIVITY", "severity": "LOW"}
    ]

    CACHE["events"] = events
    return events
