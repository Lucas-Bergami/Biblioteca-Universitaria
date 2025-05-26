from database_connection import conectar

def criar_obra(titulo, ano_publicacao, edicao, id_editora):
    conexao = conectar()
    cursor = conexao.cursor()
    try:
        sql = "INSERT INTO Obras (titulo, ano_publicacao, edicao, id_editora) VALUES (%s, %s, %s, %s)"
        valores = (titulo, ano_publicacao, edicao, id_editora)
        cursor.execute(sql, valores)
        conexao.commit()
        print("Obra criada com sucesso!")
    except mysql.connector.Error as err:
        print(f"Erro ao criar obra: {err}")
    finally:
        cursor.close()
        conexao.close()

def listar_obras():
    conexao = conectar()
    cursor = conexao.cursor(dictionary=True)
    try:
        cursor.execute("SELECT * FROM Obras")
        obras = cursor.fetchall()
        return obras
    except mysql.connector.Error as err:
        print(f"Erro ao listar obras: {err}")
    finally:
        cursor.close()
        conexao.close()
