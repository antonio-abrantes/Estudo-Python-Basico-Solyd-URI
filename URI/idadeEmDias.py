# -*- coding: utf-8 -*-
ano = 0
mes = 0

dias = int(input())

dia = (dias % 365) % 30

while True:
    if dias >= 365:
        dias = dias - 365
        ano = ano + 1

    if (dias < 365) and (dias >= 30):
         dias = dias - 30
         mes = mes + 1

    dias = dias - 1
    if(dias == 0):
        break

print(ano, "ano(s)")
print(mes,"mes(es)")
print(dia,"dia(s)")