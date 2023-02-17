dicionario = {"Nome": 'Bruno', "Sobrenome": 'Santana',
              "Idade": '31', "Curso": 'Progamação', "Endereço": 'Nova Metrópole'}
#a) Imprima o dicionário completo
print(dicionario.items())
print(dicionario)
#b) Imprima cada um dos 5 itens separadamente
print(dicionario["Nome"])
print(dicionario["Sobrenome"])
print(dicionario["Idade"])
print(dicionario["Curso"])
print(dicionario["Endereço"])
#c) Exclua a chave CURSO do dicionário
del dicionario["Curso"]
#d) Altere o ULTIMO NOME para Lopes
dicionario["Sobrenome"] = 'Lopes'
#e) Imprima novamente o dicionário completo
print(dicionario)
#f) Imprima apenas o endereço
print(dicionario["Endereço"])
#g) Crie uma cópia do dicionário e altere Nome e Idade
dicionario2 = dicionario.copy()
dicionario2["Nome"] = 'Felipe'
dicionario2["Idade"] = '23'
#h) Imprima o segundo dicionário completo
print(dicionario2)