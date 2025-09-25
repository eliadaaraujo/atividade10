# Atividade 10 – Conversão de Unidades
# Peça ao usuário um valor em metros.
# Converta e mostre o resultado em centímetros e milímetros.

valor_em_metros = int(input("digite um valor em metros: "))
valor_em_centimetros = valor_em_metros / 100
valor_em_milimetros = valor_em_metros / 1000
print(f'esse número em centímetros é: {valor_em_centimetros} e esse número em milímetros é: {valor_em_milimetros}')
