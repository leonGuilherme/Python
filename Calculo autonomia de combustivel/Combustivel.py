def combustivel_gasto(tempo_gasto, velocidade_media, autonomia):
    distancia = tempo_gasto * velocidade_media
    combustivel = distancia / autonomia
    return combustivel


# Pedir ao usuario para inserir o tempo gasto e a velocidade media
tempo_gasto = float(input("Insira o tempo gasto (em horas): "))
velocidade_media = float(input("Insira a velocidade media (em km/h): "))

# Autonomia do Veiculo
autonomia = float(input("Insira a autonomia do veiculo: "))  # km/l

# Calcular a quantidade de combustivel gasto
combustivel = combustivel_gasto(tempo_gasto, velocidade_media, autonomia)
print(f"Combustivel gasto: {combustivel:.2f} litros")
