data_file = input("Digite o nome do arquivo: ")
n = int(input("Numero de elementos do vetor : "))
 
cadeia = list(map(int,input("\nNúmeros do vetor: ").strip().split()))[:n]
 
print("\nList is - ", cadeia)

with open (str(data_file)) as dfa_file:
    dfa_data = dfa_file.read()


dfa = eval(dfa_data)
delta = str(dfa['delta'])
Sigma = str(dfa['sigma'])
F = str(dfa['final_states'])
print('Estados: '+ str(dfa['states']))
print('\nSigma: ' + str(dfa['sigma']))    
print('\nEstado Inicial: ' + str(dfa['initial_state']))  
print('\nDelta: ' + str(dfa['delta'])) 
print('\nEstado final: ' + str(dfa['final_states']))


def simular_dfa(dfa,entrada):
    estado = dfa['initial_state']
    aceitar = False
    while entrada.length > 0:
        simbolo = entrada.pop(0)
        if simbolo not in dfa['sigma']:
            print('Simbolo nao pertence ao alfabeto do automato')
            break
        if estado not in dfa['states']:
            print('Estado nao pertence ao conjunto de estados do automato')
            break
        proximo_estado = dfa['delta'][estado][dfa['sigma'].index(simbolo)]
        estado = proximo_estado
        if

if __name__ == '__main__':
    reconhecer('babbbbabbaaaa') # aceita: >3 a's
    reconhecer('babbbb') # rejeita: < 3 a's
    reconhecer('baabbbba') # aceita: = 3 a's
    reconhecer('baaxbbba') # rejeita: x




