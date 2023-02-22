valores = []
print ('Digite o nome do aluno:')
nomeDoAluno = input('> ')
for x in range(3):
    valoresX=float(input('Digite a nota '+str(x+1)+': '))
    valores.append(valoresX)
media = ((valores[0]+valores[1]+valores[2])/3)
if media >= 7:
    print (f'{nomeDoAluno} foi aprovado com média: {media:,.2f}')
elif media <= 5:
     print (f'{nomeDoAluno} foi reprovado: {media:,.2f}')
else:
     print (f'{nomeDoAluno} está de recuperação: {media:,.2f}')

