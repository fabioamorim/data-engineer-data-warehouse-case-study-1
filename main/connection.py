import psycopg2

# Create connection
def get_connection_sql():
 
    database = "data-warehouse"
    user="root"
    password="adm123"
    host="127.0.0.1"
    port="5432"

    try:
        conn = psycopg2.connect(database=database, user=user, password=password,host=host, port=port)
    except Exception as err:
        return None
    
    return conn

# Execute query
def execute_sql(conn, sql, commit=False, *args):

    try:
        cursor = conn.cursor()
        result = cursor.execute(sql, args)
    except Exception as err:
        print(f"Error: {err}, {type(err)}")

    result = None

    if commit:
        conn.commit()
    else:
        result = cursor.fetchall()
    
    cursor.close()
    conn.close()

    return result
