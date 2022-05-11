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
            print('('+str(estado)+' , '+ str(simbolo) +') -> '+ str(proximo_estado))
            estado = proximo_estado
        except KeyError:
            print('Não foi possivel realizar a transição entre estados')

    if estado in dfa['final_states']:
        aceitar = True
    if aceitar == True:
        print('\nA cadeia foi aceita pelo automato')
        print('========================================================================================')
    else:
        print('\nA cadeia nao foi aceita pelo automato')
        print('========================================================================================')


#=====================================================================================================================
data_file = input("Digite o nome do arquivo: ")
with open (str(data_file)) as dfa_file:
    dfa_data = dfa_file.read()
dfa = eval(dfa_data)

reposta1 = input('\nVocê irá usar mais de uma cadeia? (S/N): ')
if reposta1 == 'N':
    cadeia = input('Digite a cadeia: ')
    cadeia = list(cadeia)
    print("\nCadeia: ", cadeia)
    simular_dfa(dfa,cadeia)
elif reposta1 == 'S':
    reposta2 = int(input('Digite o número de cadeias: '))
    for i in range(reposta2):
        cadeia = input('Digite a cadeia: ')
        cadeia = list(cadeia)
        simular_dfa(dfa,cadeia)
else:
    print('========================================================================================')
    print('\nResposta inválida')
    print('O programa será encerrado')
    print('\n========================================================================================')













