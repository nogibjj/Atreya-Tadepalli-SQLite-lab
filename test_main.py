"""
Test goes here

"""
from mylib.extract import extract
from mylib.transform_load import load
from mylib.query import create_query,read_query,update_query,delete_query

date=1/3/2015
dispatch="B02512"
date_test=3/1/2015

dispatch_update="B02764"
date_update=1/14/2015
active_vehicles=4923
trips=29553

def test_extract():
    extracted_data = extract()
    assert extracted_data == "data/Uber-Jan-Feb-FOIL.csv"


def test_transform_load():
    loaded_db = load()
    assert loaded_db == "Ubertrips.db"

def test_create():
    assert create_query(dispatch,date_test,1045,39) == "New row inserted successfully"


def test_read():
    assert read_query() == "Success"


def test_update():
    assert update_query(active_vehicles,trips,dispatch_update,date_update) == "Updated successfully"


def test_delete():
    assert delete_query(dispatch,date) == "Deleted succesfully"