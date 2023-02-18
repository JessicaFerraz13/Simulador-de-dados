import random
import PySimpleGUI as sg

class dado():
    def __init__(self):
        self.valorMinimo = 1
        self.valorMaximo = 6
        self.layout = [
            [sg.Text("      Simulador de dado      ", font = "Arial 25")],
            [sg.Text("")],
            [sg.Text("-", font = "Arial 70", key = "valor_dado")],
            [sg.Text("")],
            [sg.Button("    Jogar!    ", font = "Arial 15")],
            [sg.Text("")]          
        ]
        self.janela = sg.Window("Simulador de dado", layout = self.layout, element_justification = "c")
        
    def iniciar(self):
        while True:
            eventos, valores = self.janela.Read()
            try:
                if eventos == "    Jogar!    ":
                    valor = self.gerarValorDado()
                    self.janela["valor_dado"].update(valor)
                elif eventos == sg.WIN_CLOSED:
                    break
            
            except:
                print("Erro")
        
    def gerarValorDado(self):
        return random.randint(self.valorMinimo, self.valorMaximo)

Dado = dado()
Dado.iniciar()
