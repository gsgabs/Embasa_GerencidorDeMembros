from tkinter import *
from tkinter import ttk
from tkinter.ttk import Style
from PIL import Image, ImageTk
from tkcalendar import DateEntry, Calendar
from datetime import date
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

Estilo = Style(janela)
Estilo.theme_use("clam")

#Criando Frames------------------------------------------------------------------------
#Frame Logo
frame_logo = Frame(janela, width=1450, height=52, bg=cor18)
frame_logo.grid(row=0, column=0, pady=0, padx=0, sticky=NSEW)
frame_logo.grid_propagate(False)

#Frame Dados
frame_dados = Frame(janela, width=1450, height=60, bg=cor10)
frame_dados.grid(row=2, column=0, padx=0, sticky=NSEW)
frame_dados.grid_propagate(False)

#Frame Detalhes
frame_detalhes = Frame(janela, width=1450, height=300, bg=cor16)
frame_detalhes.grid(row=4, column=0, padx=10, sticky=NSEW)
frame_detalhes.grid_propagate(False)

#Frame Tabela
frame_tabela = Frame(janela, width=1450, height=308, bg=cor12)
frame_tabela.grid(row=5, column=0, pady=0, padx=10, sticky=NSEW)
frame_tabela.grid_propagate(False)


#Função de mostrar a tabela -----------------------------------------------------
def mostrar_tabela():
  tabela_nome = Label(frame_tabela_in, text="Tabela de Membros", height=1,pady=0, padx=0, relief="flat", anchor=NW, font=('Ivy 10 bold'), bg=cor1, fg=cor4)
  tabela_nome.grid(row=0, column=0, padx=0, pady=10, sticky=NSEW)

  #creating a treeview with dual scrollbars
  list_header = ['Prontuário','Nome','Data de Nascimento','Vencimento']

  df_list = []

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

  hd=["nw","nw","e","e"]
  h=[80,500,100,80]
  n=0

  for col in list_header:
   tree_membro.heading(col, text=col.title(), anchor=NW)
   #adjust the column's width to the header string
   tree_membro.column(col, width=h[n],anchor=hd[n])

   n+=1

  for item in df_list:
   tree_membro.insert('', 'end', values=item)

#Funções dos botões ------------------------------------------
#Mostra tela de cadastro
def cadastrar():
    print('membro')

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
    botao_salvar = Button(frame_detalhes, anchor=CENTER, text='Salvar'.upper(), width=10, overrelief=RIDGE, font=('Ivy 7 bold'), bg=cor14, fg=cor21)
    botao_salvar.place(x=357, y=10)

# Mostra frame tabela
def update():

    label_nome_procurar = Label(frame_detalhes, text="Procurar Aluno [Inserir Nome]", height=1, anchor=NW, font=('Ivy 10'), bg=cor12, fg=cor21)
    label_nome_procurar.place(x=10, y=30)
    entry_nome_procurar = Entry(frame_detalhes, width=40, justify="center", relief="solid",font=('Ivy 10'))
    entry_nome_procurar.place(x=10, y=60)

    botao_procurar = Button(frame_detalhes, anchor="center", text="Procurar", width=9, overrelief="ridge", font=("Ivy 7 bold"), bg=cor11, fg=cor21)
    botao_procurar.place(x=10, y=90)

    global frame_tabela_in
    frame_tabela_in = Frame(frame_tabela, width=1440, height=298, bg=cor18)
    frame_tabela_in.grid(row=0, column=0, pady=10, padx=10, sticky=NSEW)
    mostrar_tabela()
    print('Atualizar')

#Deleta algo
def deletar():
    print('Excluído com sucesso')


#Controle--------------------------------------

def control(i):
    if i == 'cadastro':
        for widget in frame_detalhes.winfo_children():
            widget.destroy()

        for widget in frame_tabela.winfo_children():
            widget.destroy()
        cadastrar()

    elif i == 'atualizar':
        for widget in frame_detalhes.winfo_children():
            widget.destroy()

        for widget in frame_tabela.winfo_children():
            widget.destroy()
        update()

    elif i == 'deletar':
        for widget in frame_detalhes.winfo_children():
            widget.destroy()

        for widget in frame_tabela.winfo_children():
            widget.destroy()
        deletar()


#Botões no topo-------------------------------------
#Botão Cadastrar Membro
imagem_cadastro = Image.open('adicionar.png')
imagem_cadastro = imagem_cadastro.resize((18,18))
imagem_cadastro = ImageTk.PhotoImage(imagem_cadastro)
botao_cadastro = Button(frame_dados, command=lambda:control('cadastro'), image = imagem_cadastro, text="Cadastro", width=100, compound=LEFT, overrelief=RIDGE, font=('Ivy 11'), bg=cor1, fg=cor21)
botao_cadastro.grid(row=1, column=0)

#Botão Atualizar Membro
imagem_atualizar = Image.open('atualizar.png')
imagem_atualizar = imagem_atualizar.resize((18,18))
imagem_atualizar = ImageTk.PhotoImage(imagem_atualizar)
botao_atualizar = Button(frame_dados, command=lambda:control('atualizar'), image = imagem_atualizar, text="Atualizar User", width=100, compound=LEFT, overrelief=RIDGE, font=('Ivy 11'), bg=cor1, fg=cor21)
botao_atualizar.grid(row=1, column=1)

#Botão Deletar Membro
imagem_excluir = Image.open('excluir.png')
imagem_excluir = imagem_excluir.resize((18,18))
imagem_excluir = ImageTk.PhotoImage(imagem_excluir)
botao_deletar = Button(frame_dados, command=lambda:control('deletar'), image = imagem_excluir, text="Deletar User", width=100, compound=LEFT, overrelief=RIDGE, font=('Ivy 11'), bg=cor1, fg=cor21)
botao_deletar.grid(row=1, column=2)

# Test --------------------------------------

#Linha
# ttk.Separator(janela, orient=HORIZONTAL).grid(row=1, columnspan=1,ipadx=1450)
# ttk.Separator(janela, orient=HORIZONTAL).grid(row=3, columnspan=1,ipadx=1450)

#Botões
ttk.Button(frame_logo, text="Quit", command=janela.destroy).grid(column=2, row=0)


#Abrir a tela ---------------------------------------
janela.mainloop()




