lista = ['olho', 'ovo', 'ada', 'ama', 'a', 'b']
contador=0

for x in range(len(lista)):
    nome = lista[x]
    if len(nome) != 1:
     if nome[0] == nome[-1]:
        contador = contador+1
        print(nome)
print (contador)