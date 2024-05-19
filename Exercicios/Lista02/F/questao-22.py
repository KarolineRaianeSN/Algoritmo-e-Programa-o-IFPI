"""
Leia a hora do início de um jogo e a hora de fim do jogo (cada hora é composta por 2 variáveis inteiras:
hora e minuto). Calcule e escreva a duração do jogo (horas e minutos), sabendo-se que o tempo
máximo de duração do jogo é de 24 horas e que ele pode iniciar-se em um dia e terminar no dia
seguinte.
"""
def main():
    hora_inicio = int(input("Digite a hora de início do jogo: "))
    minuto_inicio = int(input("Digite o minuto de início do jogo: "))
    hora_final = int(input("Digite a hora do final do jogo: "))
    minuto_final = int(input("Digite o minuto do final do jogo: "))

    tempo(hora_inicio,minuto_inicio,hora_final,minuto_final)

    
def tempo(hora_inicio,minuto_inicio,hora_final,minuto_final):
    minutos_inicio = hora_inicio * 60 + minuto_inicio
    minutos_final = hora_final * 60 + minuto_final
    tempo_jogo = minutos_final - minutos_inicio
    if tempo_jogo > 1440:
        return print("Tempo excede o tempo limite de jogo")
    else:
        hora = tempo_jogo // 60
        minuto = tempo_jogo % 60
        return print(f"O tempo de jogo é igual a {hora} horas e {minuto} minutos")




if __name__ == "__main__":
    main()