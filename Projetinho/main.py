def simular_dfa(dfa,entrada):
    estado = dfa['initial_state']
    aceitar = False
    while len(entrada) > 0:
        simbolo = entrada.pop(0)
        if simbolo not in dfa['sigma']:
            print('\nSimbolo nao pertence ao alfabeto do automato')
            print('\n========================================================================================')
            break
        elif estado not in dfa['states']:
            print('\nEstado nao pertence ao conjunto de estados do automato')
            print('\n========================================================================================')
            break
        try:
            proximo_estado = dfa['delta'][(estado,simbolo)]
            print('Estado: ' + str(estado) + ' Simbolo: ' + str(simbolo) + ' Proximo estado: ' + str(proximo_estado))
            estado = proximo_estado
        except KeyError:
            print('Não foi possivel realizar a transição entre estados')

    if estado in dfa['final_states']:
        aceitar = True
    if aceitar == True:
        print('A cadeia foi aceita pelo automato')
    else:
        print('\nA cadeia nao foi aceita pelo automato')


data_file = input("Digite o nome do arquivo: ")
cadeia = input('Digite a cadeia: ')
cadeia = list(cadeia)

print("\nCadeia: ", cadeia)

with open (str(data_file)) as dfa_file:
    dfa_data = dfa_file.read()
dfa = eval(dfa_data)


print('========================================================================================')





simular_dfa(dfa,cadeia)
    


# pedir ao usuario para digitar a cadeia
#cadeia = input("Digite a cadeia: ")

