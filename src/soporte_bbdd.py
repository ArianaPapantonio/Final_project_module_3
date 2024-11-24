#%% 
import mysql.connector 
import pandas as pd

# Config pandas para ver todas las columnas 
pd.set_option("display.max_columns", None)

#%%

## Función crear base de datos: 
def creacion_bbdd (query,contraseña,nombre_bbdd = 'None'):

    if nombre_bbdd is not None: 
        cnx = mysql.connector.connect(
            user = "root", 
            password = contraseña, 
            host = "127.0.0.1"
        )

        mycursor = cnx.cursor()

        try: 
            mycursor.execute(query)
            print(mycursor)
        except mysql.connector.Error as err: 
            print(err)
            print("Error code: ", err.errno)
            print("SQLSTATE", err.sqlstate )
            print("Message", err.msg)

    else: 
        cnx = mysql.connector.connect(
            user = "root", 
            password = contraseña, 
            host = "127.0.0.1", 
            database = nombre_bbdd)
            
        mycursor = cnx.cursor()

        try: 
            mycursor.execute(query)
            print(mycursor)

        except mysql.connector.Error as err: 
            print(err)
            print("Error code: ", err.errno)
            print("SQLSTATE", err.sqlstate )
            print("Message", err.msg)


#%%


## Función crear tablas: 

