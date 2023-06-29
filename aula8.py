nome ='Edson'
sobrenome = 'Miranda'
idade = 34
ano_nascimento = 2023 - idade
maior_de_idade = idade >= 18
altura_metros = 1.86
aprovado = altura_metros >= 1.80
requisitos = (aprovado and maior_de_idade)

print('Nome:', nome)
print('Sobrenome:', sobrenome)
print('Idade:', idade)
print('Ano de Nascimento:', ano_nascimento)
print('É maior de idade?', maior_de_idade)
print('Altura em metros:', altura_metros)
print('Aprovado ou reprovado:', aprovado)
print('preenche todos os resquisitos:', requisitos)

