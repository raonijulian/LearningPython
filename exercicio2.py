# Class
# Syntaxe

# Marca, Modelo, Ano

class Carro:
    def  __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
    
    def Entrada(self):
        print('Dando Partida')

    def Desligar(self):
        print('Estou desligando')

    def CarroInfo(self):
        print(self.marca, self.modelo, self.ano)

# Variáveis
carro1 = Carro('Ford', 'Fiesta', '2001')
carro1.Entrada()
carro1.Desligar()
carro1.CarroInfo()
carro2 = Carro('Volkswagen', 'Gol', '2004')
carro2.Entrada()
carro2.Desligar()
carro2.CarroInfo()
carro3 = Carro('Fiat', 'Palio', '2003')
carro3.Entrada()
carro3.Desligar()
carro3.CarroInfo()

