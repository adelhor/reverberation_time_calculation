#import math
from reverbTime import *
import mysql.connector

mydb = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'Y1012Jqkhkp',
    database = 'coefficient'
)

mycursor=mydb.cursor()
'''
mycursor.execute("SELECT * FROM coefficient")
result = mycursor.fetchall()
print(result)
'''

#space_type=input('What is the type of the space which you want to calculate the reverberation time? \n')
material = input('Write the material of the first surface \n')
sql = "SELECT * FROM coefficient WHERE MATERIAL = %s"
val = (material,)
mycursor.execute(sql, val)
my_material = mycursor.fetchall()
print(my_material)