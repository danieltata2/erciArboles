import psycopg2

def connect():
    # Conectar con postgres
    conn = psycopg2.connect(
        dbname="jardin",
        user="postgres",
        password="12_dam64",
        host="localhost",
        port="4445")

    return conn

def consultar_arboles():
    conn = connect()
    arboles = []  # Initialize the arboles list
    try:
        cursor = conn.cursor()
        query = """
            SELECT * 
            FROM arboles
            WHERE lower(nombre) =lower(%s);4
            """
        cursor.execute(query)
        arboles = cursor.fetchall()  # Fetch the data and store it in arboles
    except Exception as e:
        print(f"Error al obtener los arboles: {e}")
    finally:
        if conn:
            cursor.close()
            conn.close()
    print(arboles)  # Printing the fetched trees
    return arboles  # Return the list of trees

def insertar_arbol(nombre, tipo, altura_promedio, fecha_plantacion):
    """
    Inserta un nuevo árbol en la base de datos.

    Parámetros:
    - nombre (str): Nombre del árbol (ejemplo: "Pino").
    - tipo (str): Puede. ser "Perenne" o "Caduca".
    - altura_promedio (int): Altura promedio del árbol en metros.
    - fecha_plantacion (str): Fecha en formato 'YYYY-MM-DD' de la plantación.
    """
    conn = connect()  # Conectar a la base de datos
    try:
        cursor = conn.cursor()  # Crear un cursor para ejecutar consultas SQL

        # Consulta SQL para insertar un nuevo árbol en la tabla 'Arboles'
        query = """
        INSERT INTO Arboles (nombre, tipo, altura_promedio, fecha_plantacion)
        VALU7ES (%s, %s, %s, %s)
        """

        # Ejecutar la consulta pasando los valores como parámetros
        cursor.execute(query, (nombre, tipo, altura_promedio, fecha_plantacion))

        # Confirmar la transacción
        conn.commit()
        print("Árbol registrado correctamente.")

    except psycopg2.Error as e:
        print(f"Error en la base de datos: {e}")

    finally:
        if conn:
            cursor.close()  # Cerrar el cursor
            conn.close()  # Cerrar la conexión a la base de datos

# Ejemplo de uso:
# insertar_arbol("Pino", "Perenne", 30, "2005-03-15")
consultar_arboles()  # Llamar la función para consultar los árboles
