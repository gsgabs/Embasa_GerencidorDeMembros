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

tempo_de_vencimento = '+90 days'

#CRUD Create Read Update Delete

#Inserir Membro C
def inserir_membro(values):
    values.append(tempo_de_vencimento)
    query = """
        INSERT INTO Membros (nome, telefone, data_nascimento, data_inscricao, data_vencimento)
        VALUES (?, ?, ?, DATE('now'), DATE('now', ?)) 
    """
    cursor.execute(query, values)

#Checando Membro R
def read_membro():
    lista = []
    query = """
        SELECT * FROM Membros
    """
    linhas = cursor.fetchall()
    for linha in linhas:
        lista.append(linha)
    return lista

#Atualizando Membros U
def update_membro(values):
    query = """"
        UPDATE Membros Set nome = ?, telefone = ?, data_nascimento = ?, data_inscrição = ?, data_vencimento = ? WHERE prontuario = ?
    """
    cursor.execute(query, values)

#Apagando Membro D
def delete_membro(valor):
    query = "DELETE FROM Membros WHERE prontuario = ?"
    cursor.execute(query, (valor,))














