import sqlite3

from conexao import conn, cursor

#Inicializando Banco----------------------------------------------------------
# try:
#     conn = sqlite3.connect("CadastroDB.db")
#     print("Conexão com o banco de dados realizada com sucesso.")
# except sqlite3.Error as erro:
#     print("Houve um erro ao se conectar com o banco de dados: ", erro)
#     exit()

#Criando Cursor
# cursor = conn.cursor()

#Apagando tabela para testar
cursor.execute("DROP TABLE IF EXISTS Membros")

#Criando Tabela
cursor.execute("""
    CREATE TABLE IF NOT EXISTS Membros (
    prontuario INTEGER PRIMARY KEY,
    nome TEXT NOT NULL,
    telefone TEXT,
    data_nascimento DATE NOT NULL,
    data_inscricao DATE NOT NULL,
    data_vencimento DATE NOT NULL
    )
""")

tempo_de_vencimento = '+90 days'

#CRUD Create Read Update Delete-----------------------------------------------

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
    cursor.execute(query)
    linhas = cursor.fetchall()
    for linha in linhas:
        lista.append(linha)
    return lista

#Atualizando Membros U
def update_membro(values):
    query = """
        UPDATE Membros Set nome = ?, telefone = ?, data_nascimento = ?, data_inscricao = ?, data_vencimento = ? WHERE prontuario = ?
    """
    cursor.execute(query, values)

#Apagando Membro D
def delete_membro(valor):
    query = "DELETE FROM Membros WHERE prontuario = ?"
    cursor.execute(query, (valor,))

#Conexão com frontend------------------------------------------------

# def novo_membro():




#Test Area ------------------------------------------------

# Inserindo diretamente para teste
cursor.execute("""
    INSERT INTO Membros (nome, telefone, data_nascimento, data_inscricao, data_vencimento)
    VALUES
    ('Joana D Arc', '11987654321', '1412-01-06', DATE('now'), DATE('now', ?)),
    ('Cristovão Colombo', '21987654321', '1451-10-31', DATE('now'), DATE('now', ?)),
    ('Ezio Auditore', '31987654321', '1459-06-24', DATE('now'), DATE('now', ?))
""", (tempo_de_vencimento, tempo_de_vencimento, tempo_de_vencimento))


# Exemplo de uso da função inserir_membro
valores_inserir = ['Leonardo da Vinci', '40028922', '1401-01-01']
inserir_membro(valores_inserir)

valores_atualizar = ('Abraham Lincoln', '3321156', '1777-02-04', '2025-01-01', '2025-06-01', 4)
update_membro(valores_atualizar)

delete_membro(3)

for item in read_membro():
    print(item)

#Finalizando --------------------------------------------------

# Salvando as alterações
conn.commit()

# Fechando a conexão
conn.close()




