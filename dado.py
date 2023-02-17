import random

class dado():
    def __init__(self):
        self.valorMinimo = 1
        self.valorMaximo = 6
        self.mensagem = "Você gostaria de gerar um novo valor para o dado? "

    def iniciar(self):
        resposta = input(self.mensagem)
        resposta = resposta.lower()
        if resposta == "sim" or resposta == "s":
            self.gerarValorDado()
            self.iniciar()
        elif resposta == "não" or resposta == "nao" or resposta == "n":
            print("Obrigada por utilizar nossa aplicação!")
        else:
            print("Digite 'sim' ou 'não'!")
            self.iniciar()
        
    def gerarValorDado(self):
        print(random.randint(self.valorMinimo, self.valorMaximo))

Dado = dado()
Dado.iniciar()
