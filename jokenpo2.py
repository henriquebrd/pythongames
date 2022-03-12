# Pacotes necessários
from random import randint
from time import sleep
from tkinter import*
import webbrowser






#Funções das opções do usuário



def op_pedra():
    vitoriaperda = randint(0,1)
    resultado = vitoriaperda
    print(vitoriaperda)
    interface2 = Tk()
    interface2.title("Resultado")
    textoinst1 = Label(interface2, text="Se o resultado exibido for 1 você ganhou se não, perdeu otário, só para lembrar você jogou pedra")
    textoinst1.grid(column=0, row=2)
    textoresultado = Label(interface2, text=vitoriaperda)
    textoresultado.grid(column=0, row=4)
    

def op_papel():
    vitoriaperda = randint(0,1)
    resultado = vitoriaperda
    print(vitoriaperda)
    interface2 = Tk()
    interface2.title("Resultado")
    textoinst1 = Label(interface2, text="Se o resultado exibido for 1 você ganhou se não, perdeu otário, só para lembrar você jogou papel")
    textoinst1.grid(column=0, row=2)
    textoresultado = Label(interface2, text=vitoriaperda)
    textoresultado.grid(column=0, row=4)


def op_tesoura():
    vitoriaperda = randint(0,1)
    resultado = vitoriaperda
    print(vitoriaperda)
    interface2 = Tk()
    interface2.title("Resultado")
    textoinst1 = Label(interface2, text="Se o resultado exibido for 1 você ganhou se não, perdeu otário, só para lembrar você jogou tesoura")
    textoinst1.grid(column=0, row=2)
    textoresultado = Label(interface2, text=vitoriaperda)
    textoresultado.grid(column=0, row=4)


def meusite():
    new=2
    site =str(input('brdsite.com: '))
    url = "https://brdsite.com/"


    webbrowser.open(url,new=new)




#interface gráfica
interface = Tk()
interface.title("Jokenpo")
texto1 = Label(interface, text="Escolha uma das opções do jogo")
texto1.grid(column=0, row=2)
botaopedra = Button(interface, text="Pedra", command=op_pedra)
botaopapel = Button(interface, text="Papel", command=op_papel)
botaotesoura = Button(interface, text="Tesoura", command=op_tesoura)
botaopedra.grid(column=0, row=4)
botaopapel.grid(column=0, row=5)
botaotesoura.grid(column=0, row=6)
acessarmeusite = Button(interface, text="Ver meu site", command=meusite)
acessarmeusite.grid(column=0, row=7)
textosite = Label(interface, text="Quando fechar a janela pressione enter no terminal para abrir o navegador web caso tenha clicado em ver meu site")
textosite.grid(column=0, row=9)

interface.mainloop()