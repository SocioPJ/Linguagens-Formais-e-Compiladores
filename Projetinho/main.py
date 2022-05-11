data_file = input("Digite o nome do arquivo: ")
cadeia = input('Digite a cadeia: ')
cadeia = list(cadeia)

print("\nCadeia: ", cadeia)

with open (str(data_file)) as dfa_file:
    dfa_data = dfa_file.read()
dfa = eval(dfa_data)


print('========================================================================================')


def simular_dfa(dfa,entrada):
    estado = dfa['initial_state']
    aceitar = False
    while len(entrada) >= 0:
        simbolo = entrada.pop(0)
        if simbolo not in dfa['sigma']:
            print('\nSimbolo nao pertence ao alfabeto do automato')
            print('\n========================================================================================')
            break
        elif estado not in dfa['states']:
            print('\nEstado nao pertence ao conjunto de estados do automato')
            print('\n========================================================================================')
            break
        proximo_estado = dfa['delta'][estado][dfa['sigma'].index(str(simbolo))]
        print('Estado: ' + str(estado) + ' Simbolo: ' + str(simbolo) + ' Proximo estado: ' + str(proximo_estado))
        estado = proximo_estado
        
        if dfa['delta',estado] not in dfa['delta']:
            print('Nao foi possivel realizar transicao entre os estados')
            
    
    if estado in dfa['final_states'] and len(entrada) == 0:
        aceitar = True

    if aceitar == True:
        print('A cadeia foi aceita pelo automato')
    else:
        print('\nA cadeia nao foi aceita pelo automato')


simular_dfa(dfa,cadeia)
    


# pedir ao usuario para digitar a cadeia
#cadeia = input("Digite a cadeia: ")

