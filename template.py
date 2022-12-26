#import library
from sqlitedl import get, create, update

#create Class

#declaration of the creation class
#name = create(FileName)
db_create = create('data.db')

#use the create.db function to create a database
#create.db(table_name, key_name, variables)
db_create.db('cars', 'model', 'year_of_release INT')

#use the create.line function to create a row in the database
#create.line(table_name, variables, (value1, value2, ...))
db_create.line('cars', 'model, year_of_release', ('hyundai tucson', 2022))

#update Class

#declaration of the update class
#name = update(FileName, table_name, key_name)
db_update = update('data.db', 'cars', 'model')

#use the update.intvar function to update the variable in the database (int, float)
#update.intvar(key_value, variable_name, mode, change)
db_update.intvar('hyundai tucson', 'year_of_release', '+', 2) #adding 2 to the variable
db_update.intvar('hyundai tucson', 'year_of_release', '-', 2) #subtracting 2 from a variable
db_update.intvar('hyundai tucson', 'year_of_release', '/', 2) #dividing a variable by 2
db_update.intvar('hyundai tucson', 'year_of_release', '*', 2) #multiplying a variable by 2
db_update.intvar('hyundai tucson', 'year_of_release', 'set', 2000) #setting a new variable value
#use the update.charvar function to update the variable in the database (string)
#update.charvar(key_value, variable_name, change)
db_update.charvar('hyundai tucson', 'model', 'hyundai solaris')

#get Class

#declaration of the getting class
#name = get(FileName, table_name)
db_get = get('data.db', 'cars')

#use the function get.line to get a database row by a key value (returns a list!)
#name = get.line(key_name, key_value)
model = db_get.line('model', 'hyundai solaris')
print(model[0])
