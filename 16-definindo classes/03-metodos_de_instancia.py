# metodo de instancia, classe e estatico
class Evento:
    def metoro_instancia(self):
        return ("metodo de instancia", self)
    
    # Definição: Os métodos de classe são declarados usando a palavra-chave 
    # @classmethod antes da definição do método. Geralmente, o primeiro 
    # parâmetro de um método de classe é cls, que se refere à própria classe.
    @classmethod
    def metodo_classe(cls):
        return ("metodo de classe chamdo", cls)
    
    @staticmethod
    def metodo_estatico():
        return "estatico chamado"