"""
class MinhaClasse: #Pascal

    def __init__(self):
        self.meu_atributo = 'Olá, Mundo!' # atributo é a característica

    def meu_metodo(self): # método é a ação // self re referencia a classe 
        print('Estou no método!')

    def meu_metodo2(self, num, mult): # self re referencia a classe 
        return num * mult

objeto = MinhaClasse () # instancia do objeto
result = objeto.meu_metodo2(3,2)
print(result)
objeto.meu_metodo()

"""
class ControleRemoto:
    def __init__(self, televisao, comodo):
        self.televisao = televisao
        self.comodo = comodo

    def avancar_canal(self):
        print('Canal avancado')
    
    def voltar_canal(self):
        print('Voltar o canal')
    
    def escolher_canal(self, canal):
        print(f'Alterado para o canal {canal}')

controle_sala = ControleRemoto('Samsung', 'sala')
print(controle_sala.comodo)
print(controle_sala.televisao)
controle_sala.avancar_canal()
controle_sala.escolher_canal(12)
