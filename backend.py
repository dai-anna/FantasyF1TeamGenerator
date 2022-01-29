from fastapi import FastAPI
import requests
import uvicorn
import pandas as pd

app = FastAPI()


@app.get("/")
def root():
    r = requests.get("http://ergast.com/api/f1/current/last/results.json")
    data = r.json()["MRData"]["RaceTable"]["Races"][0]["Results"]
    return data


if __name__ == "__main__":
    uvicorn.run(app, port=8080, host="0.0.0.0")
