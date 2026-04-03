from fastapi import FastAPI

app = FastAPI(title="Antifraud Bot Backend")

@app.get("/")
def root():
    return {"message": "Қазақ anti-fraud bot іске қосылды"}