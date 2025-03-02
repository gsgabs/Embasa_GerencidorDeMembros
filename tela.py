from tkinter import *
from tkinter import ttk
from tkinter.ttk import Style
from PIL import Image, ImageTk


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
frame_dados = Frame(janela, width=1450, height=75, bg=cor10)
frame_dados.grid(row=2, column=0, padx=0, sticky=NSEW)
frame_dados.grid_propagate(False)

#Frame Detalhes
frame_detalhes = Frame(janela, width=1450, height=200, bg=cor14)
frame_detalhes.grid(row=4, column=0, padx=10, sticky=NSEW)
frame_detalhes.grid_propagate(False)

#Frame Tabela
frame_tabela = Frame(janela, width=1450, height=200, bg=cor7)
frame_tabela.grid(row=5, column=0, pady=0, padx=10, sticky=NSEW)
frame_tabela.grid_propagate(False)

#Função para cadastrar alunos
def membro():
    print('membro')

def update():
    print('Atualizar')

#Controle--------------------------------------

def control(i):
    if i == 'cadastro':
        for widget in frame_detalhes.winfo_children():
            widget.destroy()

        for widget in frame_tabela.winfo_children():
            widget.destroy()

        membro()
    elif i == 'atualizar':
        for widget in frame_detalhes.winfo_children():
            widget.destroy()

        for widget in frame_tabela.winfo_children():
            widget.destroy()

        update()




#Botões-------------------------------------
#Botão Cadastrar Membro
imagem_cadastro = Image.open('adicionar.png')
imagem_cadastro = imagem_cadastro.resize((18,18))
imagem_cadastro = ImageTk.PhotoImage(imagem_cadastro)
botao_cadastro = Button(frame_dados, command=lambda:control('cadastro'), image = imagem_cadastro, text="Cadastro", width=100, compound=LEFT, overrelief=RIDGE, font=('Ivy 11'), bg=cor1, fg=cor21)
# botao_cadastro.place(x=10, y=30)
botao_cadastro.grid(row=1, column=0)

#Botão Atualizar Membro
imagem_atualizar = Image.open('atualizar.png')
imagem_atualizar = imagem_atualizar.resize((18,18))
imagem_atualizar = ImageTk.PhotoImage(imagem_atualizar)
botao_atualizar = Button(frame_dados, command=lambda:control('atualizar'), image = imagem_atualizar, text="Atualizar User", width=100, compound=LEFT, overrelief=RIDGE, font=('Ivy 11'), bg=cor1, fg=cor21)
botao_atualizar.grid(row=1, column=1)

# Test --------------------------------------

#Linha
# ttk.Separator(janela, orient=HORIZONTAL).grid(row=1, columnspan=1,ipadx=1450)
# ttk.Separator(janela, orient=HORIZONTAL).grid(row=3, columnspan=1,ipadx=1450)

#Botões
ttk.Label(frame_tabela, text="Hello World!").grid(row=1, column=1)
ttk.Button(frame_logo, text="Quit", command=janela.destroy).grid(column=2, row=0)


#Abrir a tela ---------------------------------------
janela.mainloop()




