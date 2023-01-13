# Simulador de dado
# Simular o uso de um dado, gerando um valor de 1 até 6

import random

class SimuladorDeDado:
    def __init__(self):
        self.valor_minimo = 1
        self.valor_maximo = 6
        self.mensagem = "quieres generar un valor nuevo para el dado?"
    
    def Iniciar(self):
        resposta = input(self.mensagem)
        try:
            if resposta == "sim" or resposta == "s":
                self.GerarValorDoDado()
            elif resposta == "no" or resposta == "n":
                print ("gracias adios")
            else:
                print ("si o no unicamente")
        except:
            print("error de tipo de respuesta")

    def GerarValorDoDado(self):
        print(random.randint(self.valor_minimo, self.valor_maximo))

simulador = SimuladorDeDado()
simulador.Iniciar()