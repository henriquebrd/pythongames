import requests
from tkinter import *
from time import sleep
parte1 = (input("Palavras loucas digite a primeira parte da palavra"))
parte2 = (input("parte 2"))
parte3 = (input("parte 3"))
parte4 = (input("parte 4"))
parte5 = (input("parte 5"))
print("Pa\n")
sleep(1)
print("La\n")
sleep(1)
print("Vra\n")

def pegar_cotacoes():
    requisicao = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")

    requisicao_dic = requisicao.json()

    cotacao_dolar = requisicao_dic['USDBRL']['bid']
    cotacao_euro = requisicao_dic['EURBRL']['bid']
    cotacao_btc = requisicao_dic['BTCBRL']['bid']

    texto = f'''
    Dólar: {cotacao_dolar}
    Euro: {cotacao_euro}
    BTC: {cotacao_btc}'''

    texto_cotacao["text"] = texto

def palavra():
    janela2 = Tk()
    janela2.title("Palavra gerada")
    texto_palavra = Label(janela2, text = parte4+parte3+parte2+parte1+parte5)
    texto_palavra.grid(column=0, row=1)
    texto2 = Label(janela2, text = "Agradeço por jogar, meu site é https://brdsite.com/ Espero que tenha gostado!")
    texto2.grid(column=0, row=2)
    autor = Label(janela2, text = "Feito por Henrique Brod Kranz")
    autor.grid(column=0, row=3)

janela = Tk()
janela.title("Palavras engraçadas e misturadas")
texto_inicial = Label(janela, text = "Clique no botão para gerar a palavra louca kkkkkkkkkk")
texto_inicial.grid(column=0, row=1)
gerarpalavra = Button(janela, text = "GERAR PALAVRA", command=palavra)
gerarpalavra.grid(column=0, row=2)

texto = Label(janela, text="Clique no botão para ver as cotações de moedas")
texto.grid(column=0, row=0, padx=10, pady=10)

botao = Button(janela, text="Buscar cotações", command=pegar_cotacoes)
botao.grid(column=0, row=4, padx=10, pady=10)

texto_resposta = Label(janela, text="")
texto_resposta.grid(column=0, row=6, padx=10, pady=10)
texto_cotacao = Label(janela, text="clique no botão para carregar")
texto_cotacao.grid(column=0, row=8)

janela.mainloop()


















print("Pronto a palavra é " + parte4 + parte3 + parte2 + parte1 + parte5)
print("Obrigado por jogar! Este jogo foi feito por Henrique Brod Kranz")
print("Esta janela será fechada em 5 segundos")
sleep(5)