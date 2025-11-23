class Quarto:
    def __init__(self, numero, tipo, disponivel):
        self.__numero = numero
        self.__tipo = tipo
        self.__disponivel = disponivel

    def get_numero(self):
        return self.__numero

    def reservar(self):
        self.__disponivel = False

    def liberar(self):
        self.__disponivel = True

    def esta_disponivel(self):
        return self.__disponivel