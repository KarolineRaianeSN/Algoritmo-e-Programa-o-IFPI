"""
Verifique a validade de uma senha fornecida pelo usuário. A senha é 1234. O algoritmo deve escrever
uma mensagem de permissão de acesso ou não.
"""
def main():
    senha = 1234
    senha_digitada = int(input("Digite a sua senha: "))

    validar_senha(senha,senha_digitada)

def validar_senha(senha_digitada,senha):
    if senha_digitada == senha:
        return print("Acesso permitido")
    else:
        return print("Acesso negado")



if __name__ == "__main__":
    main()