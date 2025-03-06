import sqlite3

try:
    conn = sqlite3.connect("CadastroDB.db")
    print("Conexão com o banco de dados realizada com sucesso.")
except sqlite3.Error as erro:
    print("Houve um erro ao se conectar com o banco de dados: ", erro)
    exit()

cursor = conn.cursor()

def fechar_conexao():
    print("Fechando conexão com o banco de dados...")
    conn.commit()
    conn.close()
