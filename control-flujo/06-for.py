buscar = 10
for numero in range(5):  # Iterable
    print(numero)
    if numero == buscar:
        print("Encontrado", buscar)
        break
else:
    print("No encontré el número buscado")

for char in "Ultimate Python":
    print(char)
