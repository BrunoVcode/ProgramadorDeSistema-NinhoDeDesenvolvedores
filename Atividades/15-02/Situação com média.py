print ('Digite o nome do aluno:')
nomeDoAluno = input('> ')
nota1 = float(input ('Digite a 1º nota: '))
nota2 = float(input ('Digite a 2º nota: '))
nota3 = float(input ('Digite a 3º nota: '))
media = ((nota1+nota2+nota3)/3)
if media >= 7:
    print (f'{nomeDoAluno} foi aprovado com média: {media:,.2f}')
elif media <= 5:
     print (f'{nomeDoAluno} foi reprovado: {media:,.2f}')
else:
     print (f'{nomeDoAluno} está de recuperação: {media:,.2f}')
