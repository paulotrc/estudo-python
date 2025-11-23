import Hospede
import Quarto

class Reserva:
    def __init__(self, hospede:Hospede, quarto:Quarto):
        self.__hospede = hospede
        self.__quarto = quarto

    __hospede:Hospede
    __quarto:Quarto

    def get_hospede(self):
        return self.__hospede
        
    def get_quarto(self):
        return self.__quarto