from tkinter import *
from tkinter import ttk
import tkinter
from tkinter.ttk import Style
from PIL import Image, ImageTk
from tkcalendar import DateEntry, Calendar
from tkinter import messagebox
from datetime import date

from main import inserir_membro, read_membro

# import filediolague


#Cores-------------------------------------------
cor1 = "#E6E6FA"  #Lavanda
cor2 = "#EE82EE"  #Violeta
cor3 = "#4B0082"  #Indigo
cor4 = "#483D8B"  #DarkSlateBlue
cor5 = "#DC143C"  #Carmesim
cor6 = "#FF0000"  #Vermelho
cor7 = "#B22222"  #Firebrick
cor8 = "#8B0000"  #Vemelho Escuro
cor9 = "#FFC0CB"  #Pink
cor10 = "#FFA500" #Orange
cor11 = "#FFD700" #Gold
cor12 = "#FFDAB9" #Pêssego
cor13 = "#ADFF2F" #Verde Amarelo
cor14 = "#00FF00" #Limão
cor15 = "#008000" #Verde
cor16 = "#66CDAA" #Água Marinha
cor17 = "#00FFFF" #Água
cor18 = "#E0FFFF" #Light Cyan
cor19 = "#40E0D0" #Turquesa
cor20 = "#00BFFF" #DeepSkyBlue
cor21 = "#36454F" #Carvão

#Criando Janela -----------------------------------------------------------
janela = Tk()
janela.title("Tela-01")
janela.geometry('1450x720')
janela.configure(background=cor20)

# Estilo = Style(janela)
# Estilo.theme_use("clam")

# Configuração das colunas da janela
janela.grid_columnconfigure(0, weight=1)  # Coluna 0 (frame_detalhes)
janela.grid_columnconfigure(1, weight=1)  # Coluna 1 (frame_tabela)

# Criando Frames ------------------------------------------------------------------------
# Frame Logo
frame_logo = Frame(janela, width=1450, height=52, bg=cor18)
frame_logo.grid(row=0, column=0, columnspan=2, pady=0, padx=0, sticky=NSEW)  # Ocupa duas colunas
frame_logo.grid_propagate(False)

# Frame Dados
frame_dados = Frame(janela, width=1450, height=60, bg=cor10)
frame_dados.grid(row=1, column=0, columnspan=2, padx=0, sticky=NSEW)  # Ocupa duas colunas
frame_dados.grid_propagate(False)

# Frame Detalhes
frame_detalhes = Frame(janela, width=650, height=608, bg=cor16)
frame_detalhes.grid(row=2, column=0, padx=10, pady=10, sticky=NSEW)
frame_detalhes.grid_propagate(False)

# Frame Tabela
frame_tabela = Frame(janela, width=800, height=608, bg=cor12)
frame_tabela.grid(row=2, column=1, pady=10, padx=10, sticky=NSEW)
frame_tabela.grid_propagate(False)

# frame_tabela_in = Frame(frame_tabela, width=800, height=603, bg=cor18)
# frame_tabela_in.grid(row=0, column=0, pady=10, padx=10, sticky=NSEW)

#Variáveis Globais
global entry_nome, entry_telefone, entry_data_nascimento

#Função dos botões da tela cadastrar---------------------------------------------
def salvar_membro():
    nome_membro = str(entry_nome.get())
    telefone_membro = str(entry_telefone.get())
    data_nascimento_membro = str(entry_data_nascimento.get())

    lista = [nome_membro, telefone_membro, data_nascimento_membro]

    for item in lista:
        if item == '':
            messagebox.showerror('Erro', 'preencha todos os campos')
            return

    #inserindo no banco
    inserir_membro(lista)

    messagebox.showinfo('Sucesso', 'Novo membro cadastrado com sucesso.')

    # entry_nome.delete(0,END)
    # entry_telefone.delete(0, END)
    # entry_data_nascimento(0, END)

    mostrar_tabela()

#Atualizar membro
def update_membro():

    try:
        tree_itens = tree_membro.focus()
        tree_dictionary = tree_membro.item(tree_itens)
        tree_lista = tree_dictionary['values']

        valor_id = tree_lista[0]

        entry_nome.insert(0, tree_lista[1])
        entry_telefone.insert(0, tree_lista[2])
        entry_data_nascimento.insert(0, tree_lista[3])

        def update():
            nome_membro = str(entry_nome.get())
            telefone_membro = str(entry_telefone.get())
            data_nascimento_membro = str(entry_data_nascimento.get())

            lista = [nome_membro, telefone_membro, data_nascimento_membro, valor_id]

            for item in lista:
                if item == '':
                    messagebox.showerror('Erro', 'preencha todos os campos')
                    break

            # atualizando no banco
            update_membro(lista)

            messagebox.showinfo('Sucesso', 'Novo membro cadastrado com sucesso.')

            entry_nome.delete(0, END)
            entry_telefone.delete(0, END)
            entry_data_nascimento(0, END)

            # mostrar_tabela()
    except:
        print("Hello Morning")

#Função de mostrar a tabela -----------------------------------------------------
def mostrar_tabela():
    global frame_tabela_in
    frame_tabela_in = Frame(frame_tabela, width=800, height=603, bg=cor18)
    frame_tabela_in.grid(row=0, column=0, pady=10, padx=10, sticky=NSEW)
    tabela_nome = Label(frame_tabela_in, text="Tabela de Membros", height=1,pady=0, padx=0, relief="flat", anchor=NW, font=('Ivy 10 bold'), bg=cor1, fg=cor4)
    tabela_nome.grid(row=0, column=0, padx=0, pady=10, sticky=NSEW)

    #creating a treeview with dual scrollbars
    list_header = ['Prontuário','Nome', 'Telefone','Data de Nascimento','Vencimento']

    df_list = read_membro()

    global tree_membro

    tree_membro = ttk.Treeview(frame_tabela_in, selectmode="extended",columns=list_header, show="headings")

    #vertical scrollbar
    vsb = ttk.Scrollbar(frame_tabela_in, orient="vertical", command=tree_membro.yview)
    #horizontal scrollbar
    hsb = ttk.Scrollbar(frame_tabela_in, orient="horizontal", command=tree_membro.xview)

    tree_membro.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
    tree_membro.grid(column=0, row=1, sticky='nsew')
    vsb.grid(column=1, row=1, sticky='ns')
    hsb.grid(column=0, row=2, sticky='ew')
    frame_tabela_in.grid_rowconfigure(0, weight=12)

    hd=["nw","nw","e","e", "e"]
    h=[80,420, 80,90,80]
    n=0

    for col in list_header:
     tree_membro.heading(col, text=col.title(), anchor=NW)
     tree_membro.column(col, width=h[n],anchor=hd[n])

     n+=1

    for item in df_list:
     tree_membro.insert('', 'end', values=item)


#Funções dos botões de cima ------------------------------------------------------------------------------------------
#Mostra tela de cadastro
def cadastrar():

    global entry_nome, entry_telefone, entry_data_nascimento

    #Campos de preencher
    #Campo nome
    label_nome = Label(frame_detalhes, text="Nome do aluno", height=1, anchor=NW, font=('Ivy 10'), bg=cor12, fg=cor21)
    label_nome.place(x=4, y=10)
    entry_nome = Entry(frame_detalhes, width=70, justify='left', relief='solid')
    entry_nome.place(x=7, y=40)

    #Campo telefone
    label_telefone = Label(frame_detalhes, text="Telefone", height=1, anchor=NW, font=('Ivy 10'), bg=cor12, fg=cor21)
    label_telefone.place(x=4, y=70)
    entry_telefone = Entry(frame_detalhes, width=35, justify='left', relief='solid')
    entry_telefone.place(x=7, y=100)

    #Campo Data de Nascimento
    label_data_nascimento = Label(frame_detalhes, text="Data de Nascimento", height=1,anchor=NW,font=('Ivy 10'), bg=cor12, fg=cor21)
    label_data_nascimento.place(x=446, y=10)
    entry_data_nascimento = DateEntry(frame_detalhes, width=18, bg=cor12, fg=cor21, borderwidth=2, year=2025)
    entry_data_nascimento.place(x=450, y=40)

    # Botões
    botao_salvar = Button(frame_detalhes, command=lambda:salvar_membro(), anchor=CENTER, text='Salvar'.upper(), width=10, overrelief=RIDGE, font=('Ivy 7 bold'), bg=cor14, fg=cor21)
    botao_salvar.place(x=357, y=10)

# Mostra frame tabela
def update():

    label_nome_procurar = Label(frame_detalhes, text="Procurar Aluno [Inserir Nome]", height=1, anchor=NW, font=('Ivy 10'), bg=cor12, fg=cor21)
    label_nome_procurar.place(x=10, y=30)
    entry_nome_procurar = Entry(frame_detalhes, width=40, justify="center", relief="solid",font=('Ivy 10'))
    entry_nome_procurar.place(x=10, y=60)

    botao_procurar = Button(frame_detalhes, anchor="center", text="Procurar", width=9, overrelief="ridge", font=("Ivy 7 bold"), bg=cor11, fg=cor21)
    botao_procurar.place(x=10, y=90)

    # global frame_tabela_in
    # frame_tabela_in = Frame(frame_tabela, width=800, height=603, bg=cor18)
    # frame_tabela_in.grid(row=0, column=0, pady=10, padx=10, sticky=NSEW)
    mostrar_tabela()
    print('Atualizar')

#Deleta algo
def deletar():
    print('Excluído com sucesso')


#Controle--------------------------------------

def control(i):
    for widget in frame_detalhes.winfo_children():
        widget.destroy()

    for widget in frame_tabela.winfo_children():
        widget.destroy()
    if i == 'cadastro':
        cadastrar()
    elif i == 'atualizar':
        update()
    elif i == 'deletar':
        deletar()

    #
    # if i == 'cadastro':
    #     for widget in frame_detalhes.winfo_children():
    #         widget.destroy()
    #
    #     for widget in frame_tabela.winfo_children():
    #         widget.destroy()
    #     cadastrar()
    #
    # elif i == 'atualizar':
    #     for widget in frame_detalhes.winfo_children():
    #         widget.destroy()
    #
    #     for widget in frame_tabela.winfo_children():
    #         widget.destroy()
    #     update()
    #
    # elif i == 'deletar':
    #     for widget in frame_detalhes.winfo_children():
    #         widget.destroy()
    #
    #     for widget in frame_tabela.winfo_children():
    #         widget.destroy()
    #     deletar()

#Botões no topo-------------------------------------
#Botão Cadastrar Membro
imagem_cadastro = Image.open('Assets/adicionar.png')
imagem_cadastro = imagem_cadastro.resize((18,18))
imagem_cadastro = ImageTk.PhotoImage(imagem_cadastro)
botao_cadastro = Button(frame_dados, command=lambda:control('cadastro'), image = imagem_cadastro, text="Cadastrar", width=100, compound=LEFT, overrelief=RIDGE, font=('Ivy 11'), bg=cor1, fg=cor21)
botao_cadastro.grid(row=1, column=0)

#Botão Atualizar Membro
imagem_atualizar = Image.open('Assets/atualizar.png')
imagem_atualizar = imagem_atualizar.resize((18,18))
imagem_atualizar = ImageTk.PhotoImage(imagem_atualizar)
botao_atualizar = Button(frame_dados, command=lambda:control('atualizar'), image = imagem_atualizar, text="Atualizar", width=100, compound=LEFT, overrelief=RIDGE, font=('Ivy 11'), bg=cor1, fg=cor21)
botao_atualizar.grid(row=1, column=1)

#Botão Deletar Membro
imagem_excluir = Image.open('Assets/excluir.png')
imagem_excluir = imagem_excluir.resize((18,18))
imagem_excluir = ImageTk.PhotoImage(imagem_excluir)
botao_deletar = Button(frame_dados, command=lambda:control('deletar'), image = imagem_excluir, text="Deletar", width=100, compound=LEFT, overrelief=RIDGE, font=('Ivy 11'), bg=cor1, fg=cor21)
botao_deletar.grid(row=1, column=2)

# Test --------------------------------------


#Botões
ttk.Button(frame_logo, text="Quit", command=janela.destroy).grid(column=2, row=0)


#Abrir a tela ---------------------------------------
janela.mainloop()




