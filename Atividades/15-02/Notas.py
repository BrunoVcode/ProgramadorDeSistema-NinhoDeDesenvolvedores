valores = []
for x in range(3):
    valoresX=(input('Escreva o número: '))
    valores.append(valoresX)
media = ((valores[0]+valores[1],valores[2])/3) 
if media >= 7:
    print ('O Aluno foi aprovado')
elif media <= 5:
    print ('O Aluno foi reprovado')
else:
    media <7 and media >5
    print ('O Aluno está de recuperação')
