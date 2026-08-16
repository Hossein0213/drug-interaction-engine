from fastapi import FastAPI

app = FastAPI(
    title = "Drug Interaction Engine",
    description = "Multi-Agent AI system for drug intreraction analysis and prediction",
    version = "0.1.0"
)


@app.get("/health")
async def health_check() -> dict[str, str]:
    return {
        "status": "healthy",
        "service": "drug-interaction-engine"
    }