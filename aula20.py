'''
#minha solução:

primeiro_valor = input("Digite um valor: ")
segundo_valor = input("Digite outro valor: ")

if primeiro_valor >= segundo_valor:
    print ("primeiro valor:", primeiro_valor ,
           "é maior ou igual que segundo valor :", segundo_valor)

elif segundo_valor >= primeiro_valor:
    print ("segundo valor:", segundo_valor, 
           "é maior ou igual que o primeiro valor :", primeiro_valor) '''

#solução do professor 

primeiro_valor = input('Digite um valor: ')
segundo_valor = input('Digite outro valor: ')

if primeiro_valor >= segundo_valor:
    print(
        f'{primeiro_valor=} é maior ou igual '
        f'ao que {segundo_valor=}'
    )
else:
    print(
        f'{segundo_valor=} é maior '
        f'do que {primeiro_valor=}'
    )