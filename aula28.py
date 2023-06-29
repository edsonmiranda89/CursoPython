'''
nome = input (" Escreva o seu nome: ")
idade = input ("Digite sua idade: ")
nome_invertido = nome [::-1]
encontrar = " "
quantia_letras = len (nome)
letra_1 = nome [0]
letra_fim = nome [-1]

if nome and idade :
    print ( f' Seu nome é: {nome}')
    print ( f' Sua idade é: {idade}')
    print ( f' Seu nome invertido fica: {nome_invertido}')

else :
    print ("Desculpe, Voce deixou campos vazios.")
        
if encontrar in nome:
    print ("Seu nome contém espaço")
else:
    print("Seu nome não contém espaço")
    

print (f'E contém ao todo {quantia_letras}'' letras')
print (f'A primeira letra do seu nome é:',letra_1)
print (f'E a última letra do seu nome é:',letra_fim)
'''
nome = input('Digite o seu nome: ')
idade = input('Digite sua idade: ')

if nome and idade:
    print(f'Seu nome é {nome}')
    print(f'Seu nome invertido é {nome[::-1]}')

    if ' ' in nome:
        print('Seu nome contém espaços')
    else:
        print('Seu nome NÃO contém espaços')

    print(f'Seu nome tem {len(nome)} letras')
    print(f'A primeira letra do seu nome é {nome[0]}')
    print(f'A última letra do seu nome é {nome[-1]}')
else:
    print("Desculpe, você deixou campos vazios.")
