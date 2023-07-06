"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""

entrada = input ( "Digite um numero inteiro: ")

try:
    entrada_int = int(entrada)
    par_impar = entrada_int % 2 == 0
    par_impar_texto = 'par'

    if par_impar:
        par_impar_texto = 'par'
        print(f'O número {entrada_int} é {par_impar_texto}')
        
    else: print (f'O numero {entrada_int} é impar')
  
except:
    print('Você não digitou um número inteiro')


    

"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.

"""
'''
entrada = input( "Digite a hora em numero inteiro ? ")
hora_now = entrada
DIA = list(range(0, 12))
TARDE = list(range(12, 18))
NOITE = list(range(18, 24))

try:
    hora_now = int(entrada)

    if hora_now in DIA:
        print ("Bom dia!")
    elif hora_now in TARDE:
        print ("Boa Tarde!")
    elif hora_now in NOITE:
        print ("Boa noite!")

    else :
        print ("Não conheço essa hora !")

except ValueError:
    print ("Por favor digite apenas um numero inteiro")
'''

"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""
'''
entrada_str = input ( "Digite o seu nome ! ")
tamanho_nome = len (entrada_str)

if entrada_str.isalpha():

 if tamanho_nome >0:
     if tamanho_nome <=4:
        print ("Seu nome é curto")
     elif tamanho_nome >= 5 and tamanho_nome <= 6:
        print ("Seu nome é normal")
     elif tamanho_nome >= 7 :
        print ("Seu nome é grande")
    # else:
      #  print ("Digite apenas o nome")    
else : 
   print ("Digite apenas o nome, sem números ou caracteres especiais") '''