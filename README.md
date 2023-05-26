# Data Warehouse Case Study 1

## Purpose

This case study has the intent to demonstrate some ETL and Data Warehouse concepts

## The enviroment

Dabase: Postgres

Language: Python 3.11

### Create the enviroment database

~~~bash
docker run --name postgres -p 5432:5432 -e POSTGRES_USER=root-e POSTGRES_PASSWORD=adm123-e POSTGRES_DB=data-warehouse -d postgres
~~~

~~~bash
sudo apt get install python3.11
sudo apt get install pip
pip install psycopg2
~~~

## Create DW and Run the ETL

~~~bash
python create_dw.py
python main.py
~~~~ 
