import pymysql

try:
    connection = pymysql.connect(
        host="127.0.0.1",
        user="root",
        password="root",  # Cambia esto por tu contraseña real de MySQL
        database="gpon"           # Cambia esto por el nombre de tu base de datos
    )
    print("Conexión exitosa a la base de datos")
except pymysql.MySQLError as e:
    print(f"Error al conectar a la base de datos: {e}")
