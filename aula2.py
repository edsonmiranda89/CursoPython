'''\r\n para quebra de linha no windows antigo.
que no meu caso o windows 
esta fazendo automatico e nao vemos então ele aceita só o \n

\r\n -> crlf (windows antigo)
\n -> lf (unix) atual
'''
print(12,34,sep="-", end='\n##')
print(56,78,sep='-', end='\n')
print(9,10,sep='-', end='\n')