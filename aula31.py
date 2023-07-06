
"""
Flag (Bandeira) - Marcar um local
None = Não valor
is e is not = é ou não é (tipo, valor, identidade)
id = Identidade

a = 10
b = 10
c = a

print(a is b)  # True
print(a is c)  # True
print(b is c)  # True

a = 10
print(id(a))
print(id(b))

"""


condicao = False
passou_no_if = None

if condicao:
    passou_no_if = True
    print('Faça algo')
else:
    print('Não faça algo')


if passou_no_if is None:
    print('Não passou no if')
else:
    print('Passou no if')