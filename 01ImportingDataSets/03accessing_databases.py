#Connection Objects
#   ->database connections
#   ->manage transactions

#   connection methods
#       -cursor() method returns a new cursor object using the connection.
#       -commit() method is used to commit any pending transaction to the 
#       database.
#       -rollback() methbod causes the database to roll back to the start of any 
#       pending transaction.
#       -close() method is used to close a database connection.

#Cursor Objects
#   ->database querys

from dbmodule import connect

#create connection object
connection = connect('datanasename', 'username', 'pswd')

#create a cursor object
cursor = connection.cursor()

#run querys
cursor.execute('select * from mytable')
results = cursor.fetchall()

#free resources
cursor.close()
connection.close()



