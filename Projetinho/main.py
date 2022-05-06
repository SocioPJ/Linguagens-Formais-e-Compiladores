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
reconhecer(cadeia)  

def reconhecer(cadeia):
    estado = str(dfa['initial_state'])
    fim_cadeia = False
    i = 0   
    try:
        while not fim_cadeia:
            if i == len(cadeia):
                fim_cadeia = True
            else:
                simbolo =  cadeia[i]
                proximo_estado = \
                    delta[estado][Sigma.index(simbolo)]
                estado = proximo_estado
            i = i + 1
        if estado in F:
            print('A cadeia ', cadeia, ' foi reconhecida')
        else:
            print('A cadeia ', cadeia, ' foi rejeitada')
    except ValueError: 
        print('A cadeia ', cadeia, ' foi rejeitada')
    except Exception as e:
        print('Erro executando o autômato: ', e)

if __name__ == '__main__':
    reconhecer('babbbbabbaaaa') # aceita: >3 a's
    reconhecer('babbbb') # rejeita: < 3 a's
    reconhecer('baabbbba') # aceita: = 3 a's
    reconhecer('baaxbbba') # rejeita: x




