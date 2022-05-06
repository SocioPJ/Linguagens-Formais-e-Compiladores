a = input("Digite o nome do arquivo: ")

with open (str(a)) as dfa_file:
    dfa_data = dfa_file.read()
print(dfa_data)

dfa = eval(dfa_data)
print(dfa)

print(dfa['states'])


print('Sigma :' + str(dfa['sigma']))    
print()