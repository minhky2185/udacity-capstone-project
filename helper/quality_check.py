import psycopg2
from helper import sql_queries

class QualityCheck:

    def check_primary_key_integrity(cur, table_name, primary_col_name):
        '''
        - Check whether any null values in the primary key of target table
        - Check whether any duplicate values in the primary key of target table
        '''
        cur.execute(sql_queries.check_null_values.format(col_name=primary_col_name, table_name=table_name))
        count_null_values = cur.fetchall()[0][0]
        cur.execute(sql_queries.check_duplicate_values.format(col_name=primary_col_name, table_name=table_name))
        count_duplicate_values = cur.fetchall()[0][0]

        if count_null_values != 0 & count_duplicate_values != 0:
            raise ValueError(f'Data quality check failed for both criteria of {table_name} table.')
        elif count_null_values != 0:
            raise ValueError(f'The primary key of {table_name} table contains null values. Data quality check failed.')
        elif count_duplicate_values != 0:
            raise ValueError(f'The primary key of {table_name} table contains duplicates values. Data quality check failed.')
        print(f'Data quality check for primary key of {table_name} table passed.')


    def check_row_number(cur, table_name):
        '''
        - Check number of rows in table
        - If there is less than 1 row in table. Data quality check failed
        '''
        cur.execute(sql_queries.check_row_number.format(table_name=table_name))
        row_number = cur.fetchall()[0][0]
        
        if row_number < 1:
            raise ValueError(f'Data quality check failed. Table {table_name} does not contain any data.')
        print(f'Data quality check on row number passed. Table {table_name} contains {row_number} rows.')
