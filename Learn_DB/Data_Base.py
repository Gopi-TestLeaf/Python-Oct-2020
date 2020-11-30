# installation:- pip install db-sqlite3

import sqlite3


# Create Connection
con = sqlite3.connect('database.db')
print("Created DB")
#************************************************************************************************

# Create Table in database.db file
con.execute('''CREATE TABLE IF NOT EXISTS flask_db(     NAME, 
                                                        USERNAME,
                                                        EMAIL,
                                                        PASSWORD)''')
print("Table Created")
#************************************************************************************************

# Insert the records
# con.execute(''' INSERT INTO flask_db(NAME, USERNAME, EMAIL, PASSWORD)
#                 VALUES('Divya', 'DivyaPraba', 'divyapraba@gmail.com', 54321)''')
# ##con.commit()
# print('Inserted records')
#************************************************************************************************

# update the records
qr = ''' UPDATE flask_db set USERNAME = 'DivyaP' WHERE NAME = 'Divya'  '''
con.execute(qr)
con.commit()
print('Updated records')
#************************************************************************************************

# Fetch all values
data = con.execute(''' SELECT * FROM flask_db ''')
print(data)

for i in data:
    print(i)
print("fetched all record")
#************************************************************************************************

# close the Connection
con.close()
print("Close DB")