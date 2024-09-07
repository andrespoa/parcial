

#isntalar el paquete de coneción de msql en la termiinal
#pip install mysql-connector-python==8.0.29
import mysql.connector

database = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="database1"
)
#ir a app.py e importar este archivo de conexion ---> 5 