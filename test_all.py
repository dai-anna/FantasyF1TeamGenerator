import pytest
import requests
from backend import root, years


def test_root():
    assert (
        str(requests.get(f"http://ergast.com/api/f1/current/driverStandings.json"))
        == "<Response [200]>"
    )
