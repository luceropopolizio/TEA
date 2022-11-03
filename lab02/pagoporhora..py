# Tendencias e Innovacion en Tecnologia Agricola (TEA)
#
from unicodedata import numeric


horas = input("horas trabajadas?")
print(horas)
print(type(horas))
valorPorHora = input("valor po hora?")
print(valorPorHora)
print(type(valorPorHora))
numeric = [int(horas) *int(valorPorHora)]
print(numeric) 