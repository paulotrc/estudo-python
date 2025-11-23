def main():
    """Função principal do programa."""
    # Instanciando a Classe Pessoa e executando os metodos dela
    p1 = Pessoa()

    print(p1.get_id())
    print(p1.get_nome())
    print(p1.get_email())

    # Instanciando a Classe Funcionario e executando os metodos dela
    f1 = Funcionario()

    f1.add_quarto("Hotel Continental", "Q1")
    f1.remover_quarto("Hotel Continental", "Q1")
    f1.registrar_hospede("Foo Pessoa", "Hotel Continental")
    f1.cancelar_reserva("Hotel Continental", "R1")

    # Instanciando a Classe Hospede e executando os metodos dela
    reservas = ["R1", "R2", "R3", "R4", "R5"]
    r1 = Hospede(reservas)

    r1.fazer_reserva("R6")
    print("Reserva efetuada com sucesso")
    r1.cancelar_reserva("R4")
    print("Reserva cancelada com sucesso")
    print(r1.consultar_reservas("R6"))
    print(r1.consultar_reservas("R4"))

    # Outras funções e lógica do programa podem ser chamadas aqui
    # Por exemplo:
    # processar_dados()
    # exibir_resultados()


class Pessoa:
    # def __init__(self, id, nome, email):
    #     self.__id = id
    #     self.__nome = nome
    #     self.__email = email

    __id = 1
    __nome = "Foo"
    __email = "foo@foo.com"

    def get_id(self):
        return self.__id

    def get_nome(self):
        return self.__nome

    def get_email(self):
        return self.__email

class Funcionario:

    def add_quarto(self, hotel, quarto):
        print("Quarto " + quarto + " adicionado ao hotel "+ hotel +" com sucesso.")

    def remover_quarto(self, hotel, quarto):
        print("Quarto " + quarto + " removido do hotel "+ hotel +" com sucesso.")

    def registrar_hospede(self, hotel, hospede):
        print("Hospede " + hospede + " registrado no hotel "+ hotel +" com sucesso.")

    def cancelar_reserva(self, hotel, reserva):
        print("Reserva " + reserva + " cancelada do hotel "+ hotel +" com sucesso.")
    

class Hospede:

    def __init__(self, reservas):
        self.__reservas = reservas

    __reservas:list

    def fazer_reserva(self, reserva):
        self.__reservas.append(reserva)

    def cancelar_reserva(self, reserva):
        self.__reservas.remove(reserva)

    def consultar_reservas(self, reserva):
        if reserva in self.__reservas:
            return reserva
        else:
            return "Reserva: " + reserva + " não encontrada."

class Quarto:
    def __init__(self, numero, tipo, disponivel):
        self.__numero = numero
        self.__tipo = tipo
        self.__disponivel = disponivel


class Reserva:
    def __init__(self, hospede, quarto):
        self.__hospede = hospede
        self.__quarto = quarto

    __hospede:Hospede
    __quarto:Quarto

if __name__ == "__main__":
    # O ponto de entrada do programa
    main()
