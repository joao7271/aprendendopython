defeitos = {1: 0, 2: 0, 3: 0, 4: 0}
total_mouse = 0
list_mouse = {}
try:
    print("Bem-vindo ao nosso software!\n")
    id_mouse = input("ID do mouse ou 'sair' para encerrar: ")
    while id_mouse != 'sair':
        defeito = 0
        if id_mouse in list_mouse:
            id_mouse = input("\nID já existente! Insira uma ID não cadastrada ou 0 para sair: ")
            if id_mouse not in list_mouse:
                list_mouse[id_mouse] = defeito
        else:
            list_mouse[id_mouse] = defeito
        print("\nLista de defeitos:")
        print(f"\n1 - Sem esfera")
        print("2 - Quebrado")
        print("3 - Trocar cabo")
        print("4 - Apenas Limpar\n")
        print("Digite o número correspondente ao erro.\nOBS: Não use letras, apenas numeros.\n")
        defeito = int(input("Digite o defeito: "))
        if id_mouse in list_mouse.keys():
            list_mouse[id_mouse] = defeito
        while defeito >= 5 or defeito <= 0:
            defeito = int(input("\nDefeito inexistente! Por favor digite um defeito válido para continuar: "))
            if defeito <= 5 or defeito >= 0:
                list_mouse[id_mouse] = defeito
        id_mouse = input(f"\nDigite o ID do mouse ou 'sair' para encerrar: ")
        defeitos[defeito] += 1
        total_mouse += 1
    try:
        per_def1 = defeitos[1] / total_mouse * 100
        per_def2 = defeitos[2] / total_mouse * 100
        per_def3 = defeitos[3] / total_mouse * 100
        per_def4 = defeitos[4] / total_mouse * 100
        print(f"\nTotal de mouses analisados é: {total_mouse}\n")
        print('|',('-' * 81),'|')
        print("|Tipo de Defeito:                                      Quantidade       Percentual  |")
        print('|',('-' * 81),'|')
        print(f"1 - Sem esfera                                                {defeitos[1]}                {per_def1}")
        print(f"2 - Quebrado                                                  {defeitos[2]}                {per_def2}")
        print(f"3 - Trocar Cabo                                               {defeitos[3]}                {per_def3}")
        print(f"4 - Apenas LImpar                                             {defeitos[4]}                {per_def4}\n")
    except ZeroDivisionError:
        print("\nVoce finalizou o programa. Até mais!")
    else:
        print("ID's registradas no sistema: ")
        for ids, defeitos in list_mouse.items():
            if defeitos == 1:
                defeitos = 'Sem Esfera'
            elif defeitos == 2:
                defeitos = 'Quebrado'
            elif defeitos == 3:
                defeitos = 'Trocar Cabo'
            elif defeitos == 4:
                defeitos = 'Apenas Limpar'
            print(f"ID: {ids} = {defeitos}")
        print("\nObrigado por utilizar nosso software. Até mais!")
except ValueError:
    print("Você não digitou uma ID válida. O software será encerrado!")
