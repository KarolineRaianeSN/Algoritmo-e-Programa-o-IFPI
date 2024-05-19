"""
Leia a quantidade de horas aula dadas por dois professores e o valor por hora recebido por cada um.
Escreva na tela qual dos professores tem salário total maior.
"""
def main():
    horas_prof_A = int(input("Digite o número de horas trabalhadas pelos professor A: "))
    valor_por_hora_A= int(input("Digite quanto o professor A recebe por hora: "))
    horas_prof_B = int(input("Digite o número de horas trabalhadas pelos professor B: "))
    valor_por_hora_B= int(input("Digite quanto o professor B recebe por hora: "))

    maior_salario = salario(horas_prof_A,horas_prof_B,valor_por_hora_A,valor_por_hora_B)
    print(f"O maior salário é o do {maior_salario} ")


def salario(horas_prof_A,horas_prof_B,valor_por_hora_A,valor_por_hora_B):
    salarioA = horas_prof_A * valor_por_hora_A
    salarioB = horas_prof_B * valor_por_hora_B
    if salarioA > salarioB:
        return "professor A"
    else:
        return "professor B"

if __name__ == "__main__":
    main()