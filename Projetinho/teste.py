


data_file = input("Digite o nome do arquivo: ")
with open (str(data_file)) as dfa_file:
    dfa_data = dfa_file.read()
cadeia = input('Digite a cadeia: ')
cadeia = list(cadeia)
print("\nCadeia: ", cadeia)

dfa = eval(dfa_data)
print(dfa)
states = (dfa['states'])
states = str(states)
print(states.replace("{", "[").replace("}", "]"))

#print(dfa['sigma'])

def simular_dfa(dfa,entrada):
    entrada = []
    estado = dfa['initial_state']
    aceitar = False
    while len(entrada) > 0:
        simbolo = entrada.pop(0)
        if simbolo not in dfa['sigma']:
            print('Simbolo nao pertence ao alfabeto do automato')


simular_dfa(dfa,cadeia)