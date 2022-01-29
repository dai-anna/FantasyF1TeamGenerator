from fastapi import FastAPI
import requests
import uvicorn

app = FastAPI()

rand_driver_idx = 0


@app.get("/")
def root():
    r = requests.get(f"http://ergast.com/api/f1/current/driverStandings.json")
    data = r.json()["MRData"]["StandingsTable"]["StandingsLists"][0]["DriverStandings"][
        rand_driver_idx
    ]["Driver"]
    # ["Driver"]  # []["givenName"]
    output = "The current year's winner is number: {0}, {1} {2} ({3})! For other years, input year (between 2005-2021) at the end of the URL (e.g. /2020)".format(
        data["permanentNumber"], data["givenName"], data["familyName"], data["code"]
    )
    return output


@app.get("/{year}")
def years(year):
    if int(year) >= 2005:
        r = requests.get(f"http://ergast.com/api/f1/{year}/driverStandings.json")
        data = r.json()["MRData"]["StandingsTable"]["StandingsLists"][0][
            "DriverStandings"
        ][rand_driver_idx]["Driver"]
        # ["Driver"]  # []["givenName"]
        output = "The winner in {4} is number: {0}, {1} {2} ({3})!".format(
            data["permanentNumber"],
            data["givenName"],
            data["familyName"],
            data["code"],
            year,
        )
    else:
        output = "Uhh... sorry we don't have this data :("
    return output


if __name__ == "__main__":
    uvicorn.run(app, port=8080, host="0.0.0.0")
