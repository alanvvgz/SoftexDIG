def login():

    usuario = input("Digite o login: ")
    senha = int(input("Digite a senha: "))

    if usuario == "Santa Cruz" and senha == 1234:
        print("SANTA CRUZ!")
    else:
        print("ALTOS!")
        return login()

login()  
