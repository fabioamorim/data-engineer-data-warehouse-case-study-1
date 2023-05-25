import connection
import tools
import datetime

def insert_into_customer(order):
    sql = f"INSERT INTO production.dim_customer (id, name, segment, current, start_date) VALUES (%s, %s, %s, %s, %s)"

    conn = connection.get_connection_sql()

    qnt_id_customer, qnt_customer = len(select_id_customer(order._customer.id)), len(select_customer(order))

    if qnt_id_customer == 0:
        connection.execute_sql(conn, sql, True, order._customer.id, order._customer.name, order._customer.segment, True, datetime.datetime.now())

    else:
        if qnt_customer == 0:

            conn = connection.get_connection_sql()
            sql = f"UPDATE production.dim_product set current=%s, end_date=%s WHERE id=%s AND current=%s"
            connection.execute_sql(conn, sql, True, False, datetime.datetime.now(), order._customer.id, True )

            conn = connection.get_connection_sql()
            sql = f"INSERT INTO production.dim_customer (id, name, segment, current, start_date) VALUES (%s, %s, %s, %s, %s)"
            connection.execute_sql(conn, sql, True, order._customer.id, order._customer.name, order._customer.segment, False, datetime.datetime.now())


def insert_into_product(order):

    sql = f"INSERT INTO production.dim_product (id, name, category, sub_category, current, start_date) values (%s, %s, %s, %s, %s, %s)"

    conn = connection.get_connection_sql()

    qnt_id_product, qnt_product = len(select_id_product(order._product.id)), len(select_product(order))

    if qnt_id_product == 0: 
        connection.execute_sql(conn, sql, True, order._product.id, order._product.name, order._product.category, order._product.sub_category, True, datetime.datetime.now())
        
    else:
        if qnt_product == 0:

            conn = connection.get_connection_sql()
            sql = f"UPDATE production.dim_product set current=%s, end_date=%s WHERE id=%s AND current=%s"
            connection.execute_sql(conn, sql, True, False,datetime.datetime.now(), order._product.id, True)

            conn = connection.get_connection_sql()
            sql = f"INSERT INTO production.dim_product (id, name, category, sub_category, current, start_date) values (%s, %s, %s, %s, %s, %s)"
            connection.execute_sql(conn, sql, True, order._product.id, order._product.name, order._product.category, order._product.sub_category, True, datetime.datetime.now())

def insert_into_location(order):
    
    sql = f"INSERT INTO production.dim_location (country, city, state, postal_code, region) values (%s, %s, %s, %s, %s)"

    conn = connection.get_connection_sql()

    count = len(select_location(order))
    if count == 0:

        connection.execute_sql(conn, sql, True, order._location.country, order._location.city, order._location.state, order._location.postal_code, order._location.region)

def select_location(order):

    sql = f"SELECT * FROM production.dim_location WHERE country=%s AND city=%s AND state=%s AND postal_code=%s and region=%s"
    conn = connection.get_connection_sql()

    result = connection.execute_sql(conn, sql, False, order._location.country, order._location.city, order._location.state, order._location.postal_code, order._location.region)

    return result
    
def select_id_customer(id):

    sql = f"SELECT * FROM production.dim_customer WHERE id=%s"

    conn = connection.get_connection_sql()

    result = connection.execute_sql(conn, sql, False, id)

    return result

def select_customer(order):

    sql = f"SELECT * FROM production.dim_customer WHERE id=%s AND name=%s AND segment=%s"

    conn = connection.get_connection_sql()

    result = connection.execute_sql(conn, sql, False, order._customer.id, order._customer.name, order._customer.segment)

    return result

def select_id_product(id):

    sql = f"SELECT * FROM production.dim_product WHERE id=%s"

    conn = connection.get_connection_sql()

    result = connection.execute_sql(conn, sql, False, id)

    return result

def select_product(order):

    sql = f"SELECT * FROM production.dim_product WHERE id=%s AND name=%s AND category=%s AND sub_category=%s"

    conn = connection.get_connection_sql()

    result = connection.execute_sql(conn, sql, False, order._product.id, order._product.name, order._product.category, order._product.sub_category)

    return result

def insert_int_fact_table(order):

    sql = f"""  INSERT INTO production.fact_sales (id_product, id_customer, id_location, id_order_date, sale, transaction, ship_mode)
                SELECT pro.sk_id,
                    cust.sk_id,
                    loc.sk_id,
                    tim.id_time,
                    {order._sale},
                    '{order._id}',
                    '{order._ship_mode}'
                FROM production.dim_product pro , production.dim_customer cust,
                production.dim_location loc, production.dim_time tim
                where pro.id = %s
                and pro.name = %s
                and pro.category = %s
                and pro.sub_category = %s
                and cust.id = %s
                and cust.name = %s
                and cust.segment = %s
                and loc.country = %s
                and loc.city = %s
                and loc.state = %s
                and loc.postal_code = %s
                and loc.region = %s
                and tim.full_date = %s;
            """
    
    conn = connection.get_connection_sql()

    result = connection.execute_sql(conn, sql, True,   order._product.id, 
                                                order._product.name,
                                                order._product.category,
                                                order._product.sub_category,
                                                order._customer.id,
                                                order._customer.name,
                                                order._customer.segment,
                                                order._location.country,
                                                order._location.city,
                                                order._location.state,
                                                order._location.posta_code,
                                                order._location.region,
                                                tools.format_date(order._date)
                            )
