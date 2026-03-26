from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"status": "ok", "service": "platform-cicd-system"}


@app.get("/health")
def health_check():
    return {"status": "healthy"}