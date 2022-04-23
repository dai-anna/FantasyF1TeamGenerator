from fastapi import FastAPI
import uvicorn
from functions import current_standings, years_standings

# import requests

# rand_driver_idx = 0


# def current_standings():
#     r = requests.get("http://ergast.com/api/f1/current/driverStandings.json")
#     data = r.json()["MRData"]["StandingsTable"]["StandingsLists"][0]["DriverStandings"][
#         rand_driver_idx
#     ]["Driver"]
#     num = data["permanentNumber"]
#     fname = data["givenName"]
#     lname = data["familyName"]
#     code = data["code"]
#     output = f"The current year's winner is number: {num}, {fname} {lname} ({code})! "
#     return output


# def years_standings(year):
#     if int(year) >= 2005:
#         r = requests.get(f"http://ergast.com/api/f1/{year}/driverStandings.json")
#         data = r.json()["MRData"]["StandingsTable"]["StandingsLists"][0][
#             "DriverStandings"
#         ][rand_driver_idx]["Driver"]
#         num = data["permanentNumber"]
#         fname = data["givenName"]
#         lname = data["familyName"]
#         code = data["code"]
#         output = f"The winner in {year} is number: {num}, {fname} {lname} ({code})! "
#     else:
#         output = "Uhh... sorry we don't have this data :("
#     return output

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
