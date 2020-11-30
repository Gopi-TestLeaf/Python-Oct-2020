import sqlite3

from Learn_DB.Test_Data import TestData


def get_connection(file_name):
    con = sqlite3.connect(file_name)
    print('Created Table')
    return con


def create_table(con, table_name):
    con.execute(f'''CREATE TABLE IF NOT EXISTS {table_name}(fname, lname, email, pwd)''')
    print("Table Created")


def insert_records(con, table_name, obj):
    data = f''' INSERT INTO {table_name}(fname, lname, email, pwd) VALUES(?, ?, ?, ?)'''
    con.execute(data,(obj.fname, obj.lname, obj.email, obj.pwd))
    con.commit()
    print("inserted the records")


def close_connection(con):
    con.close()
    print("closed the connection")


if __name__ == "__main__":
    table_name = "new_table"
    con = get_connection('for_flask.db')
    create_table(con, table_name)
    obj = TestData(fname = "Gopi", lname='jai', email='gopi@gmail.com', pwd='1234')
    insert_records(con, table_name, obj)
    close_connection(con)