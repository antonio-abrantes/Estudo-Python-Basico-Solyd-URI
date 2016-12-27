import locale

def converteFahrenheit(temperatura):
    f = ((9/5) * temperatura) + 32
    return f

def converteCelsius(temperatura):
    c = (temperatura - 32) / 1.80
    return c

temp1 = converteFahrenheit(27)

temp2 = converteCelsius(temp1)

print("Temperatura em Fahrenheit", locale.format("%.2f", temp1))

print("Temperatura em Celsius", locale.format("%.2f", temp2))