import mysql.connector


try:
    conextion = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "bank_bd"
    )
except:
    print('something wrong')


cursor = conextion.cursor()

conextion.close()