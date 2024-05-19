def main():

    genero = int(input("1 - Masculino; 2 - Feminino: "))
    idade = int(input("Idade: "))
    estado_civil = int(input("Estado civíl  (1=Casado, 2=Solteiro, 3=Divorciado, 4=Viúvo): "))

    pessoas = 0
    total_masculino = 0
    total_feminino = 0
    total_idade_m = 0
    total_idade_f = 0
    total_homens_solteiros = 0
    total_mulheres_solteiras = 0
    total_divorciadas_30 = 0

    while pessoas < 100:
        if genero == 1:
            total_masculino += 1
            total_idade_m += idade
            if estado_civil == 2:
                total_homens_solteiros += 1
        elif genero == 2:
            total_feminino += 1
            total_idade_f += idade
            if estado_civil == 2:
                total_mulheres_solteiras += 1
            if estado_civil == 3 and idade > 30:
                total_divorciadas_30 += 1

        pessoas += 1

        genero = int(input("1 - Masculino; 2 - Feminino"))
        idade = int(input("Idade: "))
        estado_civil = int(input("Estado civíl  (1=Casado, 2=Solteiro, 3=Divorciado, 4=Viúvo): "))

    media_homens = total_idade_m / total_masculino
    media_mulheres = total_idade_f / total_feminino
    solteiros = total_homens_solteiros / total_masculino
    solteiras = total_mulheres_solteiras / total_feminino


    resultado = f""" 
- Média de idade dos homens: {media_homens:.2f}
- Média de idade das mulheres: {media_mulheres:.2f}
- Percentual de homens solteiros: {solteiros:.2f} %
- Percentual de mulheres solteiras: {solteiras} %
- Total de mulheres divorciadas acima de 30 anos: {total_divorciadas_30}"""

    print(resultado)






main()