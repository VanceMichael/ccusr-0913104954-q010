from fastapi import FastAPI

app = FastAPI(title="q010")

@app.get("/health")
def health():
    return {"status": "ok"}

