from fastapi import FastAPI
import uvicorn
from functions import current_standings, years_standings

app = FastAPI()

rand_driver_idx = 0


@app.get("/")
def root():
    current = current_standings()
    current = (
        str(current)
        + "For other years, input year (between 2005-2021) at the end of the URL (e.g. /2020)"
    )
    return current


@app.get("/{year}")
def years(year):
    specific_year = years_standings(year)
    specific_year = (
        str(specific_year)
        + "For other years, input year (between 2005-2021) at the end of the URL (e.g. /2020)"
    )
    return specific_year


if __name__ == "__main__":
    uvicorn.run(app, port=8080, host="0.0.0.0")
