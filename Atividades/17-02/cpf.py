while True:
    try:
        cpf = int(input('Insira seu CPF: '))
        
        if len(str(cpf)) != 11:
                print('O CPF deve ter 11 dígitos.')
                pass
        else:
                print('CPF válido.')
                break
    except:
        print('Dados inválidos.')