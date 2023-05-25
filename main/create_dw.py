import connection

data_warehouse_tables = list()

tb_dim_customer = f"""CREATE TABLE IF NOT EXISTS production.dim_customer
                    (
                        sk_id SERIAL PRIMARY KEY,
                        id VARCHAR(10) NOT NULL,
                        name VARCHAR(30) NOT NULL,
                        segment VARCHAR(30) NOT NULL,
                        current BOOL NOT NULL,
                        start_date DATE NOT NULL,
                        end_date DATE
                    );
                """

tb_dim_product = f"""CREATE TABLE IF NOT EXISTS production.dim_product
                        (
                            sk_id SERIAL PRIMARY KEY,
                            id VARCHAR(20) NOT NULL,
                            name VARCHAR(200) NOT NULL,
                            category VARCHAR(200) NOT NULL,
                            sub_category VARCHAR(200) NOT NULL,
                            current BOOL NOT NULL,
                            start_date DATE NOT NULL,
                            end_date DATE
                        );
                    """

tb_dim_location = f"""CREATE TABLE IF NOT EXISTS production.dim_location
                        (
                            sk_id SERIAL PRIMARY KEY,
                            country VARCHAR(20) NOT NULL,
                            city VARCHAR(20) NOT NULL,
                            state VARCHAR(20) NOT NULL,
                            postal_code VARCHAR(20) NOT NULL,
                            region VARCHAR(20)
                        );
                    """

tb_dim_time = f"""CREATE TABLE IF NOT EXISTS production.dim_time
                    (
                        id_time SERIAL PRIMARY KEY,
                        year NUMERIC NOT NULL,
                        month NUMERIC NOT NULL,
                        day NUMERIC NOT NULL,
                        full_date DATE NOT NULL
                    );
                """

tb_fact_sales = f"""CREATE TABLE IF NOT EXISTS production.fact_sales
                    (
                        id_product INT,
                        id_customer INT,
                        id_location INT,
                        id_order_date INT,
                        sale FLOAT,
                        transaction VARCHAR(20),
                        ship_mode VARCHAR(50),
                        PRIMARY KEY(id_product, id_customer, id_location, id_order_date, sale),
                        FOREIGN KEY (id_product) REFERENCES production.dim_product (sk_id),
                        FOREIGN KEY (id_customer) REFERENCES production.dim_customer (sk_id),
                        FOREIGN KEY (id_location) REFERENCES production.dim_location (sk_id),
                        FOREIGN KEY (id_order_date) REFERENCES production.dim_time (id_time)
                        
                    );
                """

generate_date_time = f"""INSERT INTO production.dim_time (year, month, day, full_date)
                            SELECT EXTRACT(YEAR FROM d)::INT, 
                                EXTRACT(MONTH FROM d)::INT, 
                                EXTRACT(DAY FROM d)::INT, d::DATE
                            FROM generate_series('2014-01-01'::DATE, '2024-12-31'::DATE, '1 day'::INTERVAL) d;
                      """

create_view_full_sales = f"""CREATE OR REPLACE VIEW production.v_full_sales
                                AS SELECT s.transaction as id,
                                s.ship_mode,
                                t.full_date, 
                                c.id as customer_id,
                                c.name as customer_name,
                                c.segment,
                                l.country,
                                l.city,
                                l.state,
                                l.postal_code,
                                l.region,
                                p.id as product_id,
                                p.name as product_name,
                                p.category,
                                p.sub_category,
                                s.sale
                        from production.fact_sales s left join production.dim_customer c 
                        on s.id_customer = c.sk_id left join production.dim_location l
                        on s.id_location = l.sk_id left join production.dim_product p
                        on s.id_product = p.sk_id left join production.dim_time t 
                        on s.id_order_date = t.id_time
                        Where p."current" and c."current" = True;
                        """

data_warehouse_tables.append(tb_dim_customer)
data_warehouse_tables.append(tb_dim_product)
data_warehouse_tables.append(tb_dim_location)
data_warehouse_tables.append(tb_dim_time)
data_warehouse_tables.append(tb_fact_sales)
data_warehouse_tables.append(generate_date_time)
data_warehouse_tables.append(create_view_full_sales)

for sql in data_warehouse_tables:
    conn = connection.get_connection_sql()
    connection.execute_sql(conn, sql, True)