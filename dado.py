import random
import PySimpleGUI as sg

class dado():
    def __init__(self):
        self.valorMinimo = 1
        self.valorMaximo = 6
        self.layout = [
            [sg.Text("Jogar o Dado?")],
            [sg.Button("Sim"), sg.Button("Não")]
        ]
        
    def iniciar(self):
        self.janela = sg.Window("Simulador de dado", layout = self.layout)
        self.eventos, self.valores = self.janela.Read()
        try:
            if self.eventos == "Sim":
                self.gerarValorDado()
            elif self.eventos == "Não":
                print("Obrigada por utilizar nossa aplicação!")
        except:
            print("Erro")
        
    def gerarValorDado(self):
        print(random.randint(self.valorMinimo, self.valorMaximo))

Dado = dado()
Dado.iniciar()
