import pandas as pd
"""
NYC Taxi trips dataset, arranged by day
"""
import requests

def extract(url="https://raw.githubusercontent.com/fivethirtyeight/uber-tlc-foil-response/refs/heads/master/Uber-Jan-Feb-FOIL.csv", 
            file_path="Uber-Jan-Feb-FOIL.csv"):
    """"Extract a url to a file path"""
    with requests.get(url) as r:
        with open(file_path, 'wb') as f:
            f.write(r.content)
    df=pd.read_csv(file_path)
    return file_path


