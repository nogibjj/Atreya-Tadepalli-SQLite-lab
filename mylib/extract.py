import requests
"""
NYC Taxi trips dataset, arranged by day
"""


def extract(url="https://raw.githubusercontent.com/fivethirtyeight/uber-tlc-foil-response/refs/heads/master/Uber-Jan-Feb-FOIL.csv", 
            file_path="Uber-Jan-Feb-FOIL.csv"):
    """"Extract a url to a file path"""
    with requests.get(url) as r:
        with open(file_path, 'wb') as f:
            f.write(r.content)
    return file_path


