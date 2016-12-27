import locale
kmL = 12

tempo_viagem = int(input())
vel_media = int(input())

consumoMedio = float((tempo_viagem * vel_media) / kmL)

print(locale.format("%1.3f", consumoMedio))
