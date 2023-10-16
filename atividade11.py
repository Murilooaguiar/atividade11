# Exercício Python 11: Desenvolva um programa que pergunte a distância de uma
# viagem em Km. Calcule o preço da passagem, cobrando R$0,50 por Km para
# viagens de até 200Km e R$0,45 parta viagens mais longas.

distancia= float (input("qual a distancia da viagem:"))
print(f"a distancia da sua viagem {distancia} km")
if distancia <=200:
    print (f"o preço de sua passagem será de {distancia * 0.50}")
else:
     print(f"o preço de sua passagem será de {distancia * 0.45}") 