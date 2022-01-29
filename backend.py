from fastapi import FastAPI
import requests
import uvicorn
import pandas as pd

app = FastAPI()

years = 2020
rand_driver_idx = 0


@app.get("/")
def root():
    r = requests.get(f"http://ergast.com/api/f1/{years}/driverStandings.json")
    data = r.json()["MRData"]["StandingsTable"]["StandingsLists"][0]["DriverStandings"][
        rand_driver_idx
    ]["Driver"]
    # ["Driver"]  # []["givenName"]
    return data


if __name__ == "__main__":
    uvicorn.run(app, port=8080, host="0.0.0.0")
