from Pessoa import Pessoa
# from Reserva import Reserva

class Hospede(Pessoa):

    # def __init__(self, reservas:list):
    #     self.__reservas = reservas

    __reservas = []

    def fazer_reserva(self, reserva):
        self.__reservas.append(reserva)

    def cancelar_reserva(self, reserva):
        self.__reservas.remove(reserva)

    def consultar_reservas(self, reserva):
        if reserva in self.__reservas:
            return reserva
        else:
            return "Reserva não encontrada."