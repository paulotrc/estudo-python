from Pessoa import Pessoa
import Hotel
import Quarto
import Hospede
import Reserva

class Funcionario(Pessoa):
    pass

    def add_quarto(self, hotel:Hotel, quarto:Quarto):
        hotel.add_quarto(quarto)
        print("Quarto " + str(quarto.get_numero()) + " adicionado ao hotel com sucesso.")

    def remover_quarto(self, hotel:Hotel, quarto:Quarto):
        hotel.remover_quarto(quarto)
        print("Quarto " + str(quarto.get_numero()) + " removido do hotel com sucesso.")

    def registrar_hospede(self, hotel:Hotel, hospede:Hospede):
        hotel.registrar_hospede(hospede)
        print("Hospede " + hospede.get_nome() + " registrado no hotel com sucesso.")

    def cancelar_reserva(self, hotel:Hotel, reserva:Reserva):
        hotel.cancelar_reserva(reserva)
        print("Reserva do quarto de número: " + str(reserva.get_quarto().get_numero()) + " cancelada do hotel com sucesso.")

