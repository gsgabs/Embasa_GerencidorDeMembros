import sqlite3

#Inicializando Banco----------------------------------------------------------
try:
    conn = sqlite3.connect("CadastroDB.db")
    print("Conexão com o banco de dados realizada com sucesso.")
except sqlite3.Error as erro:
    print("Houve um erro ao se conectar com o banco de dados: ", erro)
    exit()

#Criando Cursor
cursor = conn.cursor()

#Apagando tabela para testar
cursor.execute("DROP TABLE IF EXISTS Membros")

#Criando Tabela
cursor.execute("""
    CREATE TABLE IF NOT EXISTS Membros (
    prontuario INTEGER PRIMARY KEY,
    nome TEXT NOT NULL,
    telefone TEXT,
    data_nascimento DATE NOT NULL,
    data_inscricao DATE NOT NULL
    data_vencimento DATE NOT NULL
    )
""")





