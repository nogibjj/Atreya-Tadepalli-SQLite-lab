"""Query the database"""

import sqlite3

def create_query(dispatch_number,date,vehicles,trips1):
    """Query the database to insert a new row within the Ubertrips table"""
    conn = sqlite3.connect("Ubertrips.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO Ubertrips (?, ?, ?, ?)", \
    (dispatch_number,date,vehicles,trips1))
    conn.commit()
    conn.close()
    return "New row inserted successfully"

def read_query():
    """Query the database for the top 20 rows of the Ubertrips table"""
    conn = sqlite3.connect("Ubertrips.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Ubertrips LIMIT 20")
    print("Top 20 rows of the Ubertrips table")
    rows=cursor.fetchall()
    for row in rows:
        print(row)
    conn.close()
    return "Success"

def update_query(active_vehicles,trips, dispatching_base_number,date):
    """Update the records included within the Ubertrips database"""
    conn = sqlite3.connect("Ubertrips.db")
    cursor = conn.cursor()
    cursor.execute("UPDATE Ubertrips SET active_vehicles=?, trips=?, \
    WHERE (dispatching_base_number = ? AND date=?)" , \
    (active_vehicles, trips, dispatching_base_number, date,))
    print("Data Update")
    conn.commit()
    conn.close()
    return "Updated successfully"

def delete_query(dispatching_base_number,date):
    """Delete the record containing the provided dispatching base number and date"""
    conn = sqlite3.connect("Ubertrips.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Ubertrips \
    WHERE (dispatching_base_number=? AND date=?)", (dispatching_base_number,date))
    deleted = cursor.fetchall()
    cursor.execute("DELETE FROM Ubertrips \
    WHERE (dispatching_base_number=? AND date=?)", (dispatching_base_number,date))
    conn.commit()
    print("Deleting data:")
    print(deleted)
    conn.close()
    return "Deleted successfully"


