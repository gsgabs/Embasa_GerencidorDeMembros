import sqlite3
import atexit

from conexao import conn, cursor, fechar_conexao

#Criando Tabela
cursor.execute("""
    CREATE TABLE IF NOT EXISTS Membros (
    prontuario INTEGER PRIMARY KEY,
    nome TEXT NOT NULL,
    nome_responsavel TEXT,
    telefone TEXT,
    telefone2 TEXT,
    data_nascimento DATE NOT NULL,
    data_inscricao DATE NOT NULL,
    data_vencimento DATE NOT NULL
    )
""")

conn.commit()

tempo_de_vencimento = '+90 days'

#CRUD Create Read Update Delete-----------------------------------------------

#Inserir Membro C
def inserir_membro(values):
    values.append(tempo_de_vencimento)
    query = """
        INSERT INTO Membros (nome, nome_responsavel, telefone, telefone2, data_nascimento, data_inscricao, data_vencimento)
        VALUES (?, ?, ?, ?, ?, DATE('now'), DATE('now', ?)) 
    """
    cursor.execute(query, values)
    conn.commit()
    # if values[0] != "" and values[1] != "":
    #     cursor.execute(query, values)
    #     conn.commit()

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
        UPDATE Membros Set nome = ?, nome_responsavel = ?, telefone = ?, telefone2 = ?, data_nascimento = ?, data_inscricao = ?, data_vencimento = ? WHERE prontuario = ?
    """
    cursor.execute(query, values)
    conn.commit()

#Apagando Membro D
def delete_membro(valor):
    query = "DELETE FROM Membros WHERE prontuario = ?"
    cursor.execute(query, (valor,))
    conn.commit()

#Conexão com frontend------------------------------------------------

# def novo_membro():




#Test Area ------------------------------------------------

#Inserindo diretamente para teste
# cursor.execute("""
#     INSERT INTO Membros (nome, nome_responsavel, telefone, telefone2, data_nascimento, data_inscricao, data_vencimento)
#     VALUES
#     ('Joana D Arc', 'Joao Darco', '11987654321', '1199902888', '1412-01-06', DATE('now'), DATE('now', ?)),
#     ('Cristovão Colombo', 'Mrs. Cristoviana', '21987654321', '14666325', '1451-10-31', DATE('now'), DATE('now', ?)),
#     ('Ezio Auditore', 'Papa emeritus I', '31987654321', '00007000', '1459-06-24', DATE('now'), DATE('now', ?))
# """, (tempo_de_vencimento, tempo_de_vencimento, tempo_de_vencimento))


# Exemplo de uso da função inserir_membro
# valores_inserir = ['Leonardo da Vinci', '40028922', '1401-01-01']
# inserir_membro(valores_inserir)

#valores_atualizar = ('Abraham Lincoln', '3321156', '1777-02-04', '2025-01-01', '2025-06-01', 4)
#update_membro(valores_atualizar)

# delete_membro(4)

for item in read_membro():
    print(item)

print(conn)

#Finalizando --------------------------------------------------

# Salvando as alterações
conn.commit()

# Fechando a conexão
atexit.register(fechar_conexao)

