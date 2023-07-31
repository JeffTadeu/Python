import re
import sys
import random


entrada = input("Digite seu cpf: ")
cpf = re.sub(
    r'[^0-9]',
    '',
    entrada
)

sequencial = entrada == entrada[0] * len(entrada)
if sequencial:
     print("Você enviou dados sequenciais")
     sys.exit()

cpf_att = ""

for num in cpf[:9]:
        cpf_att += num 

multiplicador = 10
soma = 0
for num in cpf_att:
    soma += int(num) * multiplicador
    multiplicador -= 1 
soma = (soma * 10) % 11

primeiro_digito = soma if soma < 9 else 0
print(f'O primeiro digito é {primeiro_digito}')

#SEGUNDO DIGITO 

cpf_att = cpf_att + str(primeiro_digito)


multiplicador = 11
soma = 0

for num in cpf_att:
    soma += int(num) * multiplicador
    multiplicador -= 1 
soma = (soma * 10) % 11


segundo_digito = soma if soma <= 9 else 0
print(f'O segundo digito é {segundo_digito}')
 
cpf_gerado = str(cpf_att) + str(segundo_digito)

if cpf_gerado == cpf:
    print("Válido")
else:
    print("Inválido")
