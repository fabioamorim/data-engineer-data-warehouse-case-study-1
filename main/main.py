import connection
import controller
from csv import DictReader
import os 

source = "train.csv"

if os.path.isfile(source):
    if connection.get_connection_sql() is not None:

        controller.execute_etl(source)

