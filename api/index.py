from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import numpy as np

app = FastAPI()

# Enable CORS for all origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["POST"],
    allow_headers=["*"],
)

@app.post("/")
def check_latency(data: dict):
    regions = data.get("regions", [])
    threshold = data.get("threshold_ms", 0)
    
    result = {}
    for region in regions:
        # Sample telemetry data (replace with real metrics in prod)
        samples = np.random.randint(50, 250, size=10)  # dummy latency
        avg_latency = float(np.mean(samples))
        p95_latency = float(np.percentile(samples, 95))
        breaches = int(np.sum(samples > threshold))
        result[region] = {
            "avg_latency": avg_latency,
            "p95_latency": p95_latency,
            "avg_uptime": 99.9,  # dummy uptime
            "breaches": breaches
        }
    return result
