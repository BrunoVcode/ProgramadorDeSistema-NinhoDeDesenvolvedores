alunos = {'Alice':8, 'Pedro':7, 'Leticia':9, 'Isaac':7}
alunosOrganizados = sorted(alunos.items(), key=lambda x: x[0])
alunosOrganizadosD = sorted(alunos.items(), key=lambda x: x[0], reverse=True)
print (alunosOrganizados)
print (alunosOrganizadosD)