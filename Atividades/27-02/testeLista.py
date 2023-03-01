from rich.console import Console
from rich.markdown import Paragraph
console = Console()
paragraph = Paragraph()

console.print ('paragraph.justify.center[i][red][b]LANCHONETE[/]')
produtos=['Cachorro-quente', 'Pastel', 'Pizza', 'Refrigerante']
print(f'Quantidade de produtos registrados: {len(produtos)}')
print(f'Nome dos produtos registrados: ', end="")
print(*produtos, sep= ', ')
print('Digite o nome do produto que deve ser cadastrado')
produtos.append(input('> '))
print(*produtos, sep= ', ')
produtos.remove('Pastel')
produtos.pop(0)
print(*produtos, sep= ', ')