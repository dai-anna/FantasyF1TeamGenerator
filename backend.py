from fastapi import FastAPI
import uvicorn
from functions import current_standings, years_standings

app = FastAPI()

rand_driver_idx = 0


@app.get("/")
def root():
    return current_standings()


@app.get("/{year}")
def years(year):
    return years_standings(year)


if __name__ == "__main__":
    uvicorn.run(app, port=8080, host="0.0.0.0")
