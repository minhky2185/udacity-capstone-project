dim_station_create = '''
    CREATE TABLE dim_station (
        station_id      VARCHAR PRIMARY KEY,
        station_name    VARCHAR NOT NULL,
        station_lat     FLOAT NOT NULL,
        station_lng     FLOAT NOT NULL
    )
'''

dim_bike_type_create = '''
    CREATE TABLE dim_bike_type(
        bike_type_id    INT PRIMARY KEY,
        bike_type       VARCHAR NOT NULL
    )
'''

dim_time_create = '''
    CREATE TABLE dim_time(
        time    TIMESTAMP PRIMARY KEY,
        year    INT NOT NULL,
        month   INT NOT NULL,
        date    INT NOT NULL,
        weekday VARCHAR NOT NULL,
        hour    INT NOT NULL
    )
'''

dim_member_type_create = '''
    CREATE TABLE dim_member_type(
        member_type_id  INT PRIMARY KEY,
        member_type     VARCHAR NOT NULL
    )
'''

fact_trip_create = '''
    CREATE TABLE fact_trip(
        trip_id             VARCHAR PRIMARY KEY,
        start_time          TIMESTAMP REFERENCES dim_time(time) ON DELETE RESTRICT,
        end_time            TIMESTAMP REFERENCES dim_time(time) ON DELETE RESTRICT,
        start_station_id    VARCHAR REFERENCES dim_station(station_id) ON DELETE CASCADE,
        end_station_id      VARCHAR REFERENCES dim_station(station_id) ON DELETE CASCADE,
        temperature         FLOAT NOT NULL,
        duration            FLOAT NOT NULL,
        bike_type_id        INT REFERENCES dim_bike_type(bike_type_id) ON DELETE RESTRICT,
        member_type_id      INT REFERENCES dim_member_type(member_type_id) ON DELETE RESTRICT
    );
'''

check_duplicate_values = '''
    SELECT COUNT(*) - COUNT(DISTINCT({col_name}))
    FROM {table_name}
'''

check_null_values = '''
    SELECT COUNT(*)
    FROM {table_name}
    WHERE {col_name} is Null
'''

check_row_number = '''
    SELECT COUNT(*)
    FROM {table_name}
'''

create_table_sql = [dim_station_create, dim_bike_type_create, dim_time_create, 
                    dim_member_type_create, fact_trip_create]
