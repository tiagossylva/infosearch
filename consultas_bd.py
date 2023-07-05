from flask import request

def diesel(mysql):
    estado = request.form.get('estado')
    cursor = mysql.connection.cursor()
    query = f"SELECT Ano,MIN(Minimo) AS preco_minimo, AVG(Media) AS preco_medio," \
            f"MAX(Maximo) AS preco_maximo FROM diesel Where Estado_Sigla = '{estado}' GROUP BY Ano;"
    cursor.execute(query)
    data = cursor.fetchall()
    cursor.close()
    return (data)

def diesel_s10(mysql):
    estado = request.form.get('estado')
    cursor = mysql.connection.cursor()
    query = f"SELECT Ano,MIN(Minimo) AS preco_minimo, AVG(Media) AS preco_medio,  " \
            f"MAX(Maximo) AS preco_maximo FROM diesel_s10 Where Estado_Sigla = '{estado}' GROUP BY Ano;"
    cursor.execute(query)
    data = cursor.fetchall()
    cursor.close()
    return (data)

def etanol(mysql):
    estado = request.form.get('estado')
    cursor = mysql.connection.cursor()
    query = f"SELECT Ano,MIN(Minimo) AS preco_minimo, AVG(Media) AS preco_medio, MAX(Maximo) AS preco_maximo FROM etanol Where Estado_Sigla = '{estado}' GROUP BY Ano;"
    cursor.execute(query)
    data = cursor.fetchall()
    cursor.close()
    return (data)

def gasolina(mysql):
    estado = request.form.get('estado')
    cursor = mysql.connection.cursor()
    query = f"SELECT Ano,MIN(Minimo) AS preco_minimo, AVG(Media) AS preco_medio,  MAX(Maximo) AS preco_maximo FROM gasolina Where Estado_Sigla = '{estado}' GROUP BY Ano;"
    cursor.execute(query)
    data = cursor.fetchall()
    cursor.close()
    return (data)

def gnv(mysql):
    estado = request.form.get('estado')
    cursor = mysql.connection.cursor()
    query = f"SELECT Ano,MIN(Minimo) AS preco_minimo, AVG(Media) AS preco_medio,  MAX(Maximo) AS preco_maximo FROM gnv Where Estado_Sigla = '{estado}' GROUP BY Ano;"
    cursor.execute(query)
    data = cursor.fetchall()
    cursor.close()
    return (data)