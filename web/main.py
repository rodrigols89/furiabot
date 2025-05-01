from fastapi import FastAPI

app = FastAPI()

@app.get("/status")
def status():
    return {"status": "Bot online e funcionando 🔥"}
