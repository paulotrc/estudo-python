from Pessoa import Pessoa
from Funcionario import Funcionario
from Hospede import Hospede
from Quarto import Quarto
from Reserva import Reserva
from Hotel import Hotel

def main():
    """Função principal do programa."""
    # Instanciando a Classe Pessoa e executando os metodos dela
    p1 = Pessoa()

    print(p1.get_id())
    print(p1.get_nome())
    print(p1.get_email())

    # Instanciando a Classe Funcionario
    f1 = Funcionario()

    # Instanciando a Classe Hospede
    reservas = ["R1", "R2", "R3", "R4", "R5"]
    h1 = Hospede()
    h2 = Hospede()
    
    # Instanciando a Classe Quarto
    q1 = Quarto(1,'duplo',False)
    q2 = Quarto(2,'duplo',False)
    
    # Instanciando a Classe Reserva
    r1 = Reserva(h1, q1)
    r2 = Reserva(h2, q2)

    # Instanciando a Classe Hotel    
    list_hospedes = []
    list_quartos = []
    list_reservas = [r1, r2]
    ht = Hotel(list_hospedes, list_quartos, list_reservas)

    # Classe Funcionario: executando os metodos
    f1.add_quarto(ht, q1)
    f1.add_quarto(ht, q2)
    f1.remover_quarto(ht, q2)
    f1.registrar_hospede(ht, h1)
    f1.registrar_hospede(ht, h2)
    f1.cancelar_reserva(ht, r1)

    # Classe Hospede: executando os metodos
    h1.fazer_reserva(r1)
    h2.fazer_reserva(r2)
    print("Reserva efetuada com sucesso")
    h1.cancelar_reserva(r1)
    print("Reserva cancelada com sucesso")
    h1.cancelar_reserva(r2)
    print("Reserva cancelada com sucesso")
    print(h1.consultar_reservas(r1))
    print(h1.consultar_reservas(r2))

    # Classe Hotel: executando os metodos
    ht.add_quarto(q1)
    ht.add_quarto(q2)
    ht.registrar_hospede(h1)
    ht.remover_quarto(q2)
    ht.cancelar_reserva(r1)

    # Outras funções e lógica do programa podem ser chamadas aqui
    # Por exemplo:
    # processar_dados()
    # exibir_resultados()


if __name__ == "__main__":
    # O ponto de entrada do programa
    main()
