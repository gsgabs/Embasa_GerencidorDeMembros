from tkinter import *
from tkinter import ttk
from tkinter.ttk import Style

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


#Criando Janela
janela = Tk()
janela.title("Tela-01")
janela.geometry('1450x720')
janela.configure(background=cor20)

Estilo = Style(janela)
Estilo.theme_use("clam")

#Criando Frames
frame_logo = Frame(janela, width=1450, height=52, bg=cor18)
frame_logo.grid(row=0, column=0, pady=0, padx=0, sticky=NSEW)

#Linha
ttk.Separator(janela, orient=HORIZONTAL).grid(row=1, columnspan=1,ipadx=1450)

#Frame
frame_dados = Frame(janela, width=1450, height=65, bg=cor10)
frame_dados.grid(row=2, column=0, padx=0, sticky=NSEW)

#Linha
ttk.Separator(janela, orient=HORIZONTAL).grid(row=3, columnspan=1,ipadx=1450)

#Frame
frame_detalhes = Frame(janela, width=1450, height=200, bg=cor14)
frame_detalhes.grid(row=4, column=0, padx=10, sticky=NSEW)

frame_tabela = Frame(janela, width=1450, height=200, bg=cor7)
frame_tabela.grid(row=5, column=0, pady=0, padx=10, sticky=NSEW)



janela.mainloop()


# root = Tk()
# frm = ttk.Frame(root, padding=10)
# frm.grid()
# ttk.Label(frm, text="Hello World!").grid(column=0, row=0)
# ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=0)
# root.mainloop()


