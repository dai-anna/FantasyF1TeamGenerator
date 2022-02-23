import requests

rand_driver_idx = 0


def current_standings():
    r = requests.get("http://ergast.com/api/f1/current/driverStandings.json")
    data = r.json()["MRData"]["StandingsTable"]["StandingsLists"][0]["DriverStandings"][
        rand_driver_idx
    ]["Driver"]
    num = data["permanentNumber"]
    fname = data["givenName"]
    lname = data["familyName"]
    code = data["code"]
    output = (
        f"The current year's winner is number: {num}, {fname} {lname} ({code})! "
        + "For other years, input year (between 2005-2021) at the end of the URL (e.g. /2020)"
    )
    return output


def years_standings(year):
    if int(year) >= 2005:
        r = requests.get(f"http://ergast.com/api/f1/{year}/driverStandings.json")
        data = r.json()["MRData"]["StandingsTable"]["StandingsLists"][0][
            "DriverStandings"
        ][rand_driver_idx]["Driver"]
        num = data["permanentNumber"]
        fname = data["givenName"]
        lname = data["familyName"]
        code = data["code"]
        output = (
            f"The winner in {year} is number: {num}, {fname} {lname} ({code})! "
            + "For other years, input year (between 2005-2021) at the end of the URL (e.g. /2020)"
        )
    else:
        output = "Uhh... sorry we don't have this data :("
    return output
