import Hospede
import Quarto
import Reserva

class Hotel:
    def __init__(self, hospedes:list, quartos:list, reservas:list):
        self.__hospedes = hospedes
        self.__quartos = quartos
        self.__reservas = reservas

    __hospedes:list
    __quartos:list
    __reservas:list

    def add_quarto(self, quarto:Quarto):
        self.__quartos.append(quarto)
        print("Quarto: "+ str(quarto.get_numero()) +" adicionado com sucesso")

    def remover_quarto(self, quarto:Quarto):
        self.__quartos.remove(quarto)
        print("Quarto: "+ str(quarto.get_numero()) +" removido com sucesso")

    def registrar_hospede(self, hospede:Hospede):
        self.__hospedes.append(hospede)
        print("Hospede: "+ hospede.get_nome() +" registrado com sucesso")

    def cancelar_reserva(self, reserva:Reserva):
        if reserva in self.__reservas:
            self.__reservas.remove(reserva)
            print("Reserva para o quarto de número: "+ str(reserva.get_quarto().get_numero()) +" cancelada com sucesso")
        else:
            return "Reserva não encontrada."
        
