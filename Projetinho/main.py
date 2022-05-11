data_file = input("Digite o nome do arquivo: ")
cadeia = input('Digite a cadeia: ')
print("\nCadeia: ", cadeia)

with open (str(data_file)) as dfa_file:
    dfa_data = dfa_file.read()


dfa = eval(dfa_data)
delta = str(dfa['delta'])
Sigma = str(dfa['sigma'])
F = str(dfa['final_states'])
print('Estados: '+ str(dfa['states']))
print('Sigma: ' + str(dfa['sigma']))    
print('Estado Inicial: ' + str(dfa['initial_state']))  
print('Delta: ' + str(dfa['delta'])) 
print('Estado final: ' + str(dfa['final_states']))



def simular_dfa(dfa,entrada):
    entrada = []
    estado = dfa['initial_state']
    aceitar = False
    while len(entrada) > 0:
        simbolo = entrada.pop(0)
        if simbolo not in dfa['sigma']:
            print('Simbolo nao pertence ao alfabeto do automato')
            break
        if estado not in dfa['states']:
            print('Estado nao pertence ao conjunto de estados do automato')
            break
        proximo_estado = dfa['delta'][estado][dfa['sigma'].index(str(simbolo))]
        estado = proximo_estado
        
        if dfa['delta'][estado]not in dfa['delta']:
            print('Nao foi possivel realizar transicao entre os estados')
            break
        break
    if estado in dfa['final_states'] and len(entrada) == 0:
        aceitar = True

    if aceitar == True:
        print('A cadeia foi aceita pelo automato')
    else:
        print('A cadeia nao foi aceita pelo automato')


simular_dfa(dfa,cadeia)
    


# pedir ao usuario para digitar a cadeia
#cadeia = input("Digite a cadeia: ")

