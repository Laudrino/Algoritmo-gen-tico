import random

def main():
    matriz1 = [[random.randint(0, 1) for _ in range(11)] for _ in range(8)] # poblacion inical 
    matriz2 = [[0, 0] for _ in range(4)]
    apto = [0, 0]
    binario1 = ['' for _ in range(8)]
    num = 0
    corte = 0

    for y in range(8):
        binario1[y] = ''
        for x in range(11):  # rango 
            binario1[y] += str(matriz1[y][x])

    print("--------------Población Inicial--------------")
    for y1 in range(8):
        signo = -1 if matriz1[y1][0] == 1 else 1
        valor_absoluto = int(binario1[y1][1:-1], 2)
        valor = signo * valor_absoluto * (10 if matriz1[y1][-1] == 1 else 1)  # bit para decimal y no decimal
        print(f"{y1 + 1}) {''.join(map(str, matriz1[y1]))} = {valor}")

    while True:
        try:
            num = int(input("Ingrese un numero mayor que 0 y menor que 7: "))  # rango modificado 
            if num < 1 or num > 6:
                print("El número no está dentro del rango...")
            else:
                corte = 11 - num
                print("Número de corte:", num)
                break
        except ValueError:
            print("No es un número entero...")

    print("--------------Parejas de Población--------------")
    matriz2 = [[8, 2], [6, 1], [5, 3], [7, 4]]
    for y2 in range(4):
        print(f"{y2 + 1}) {' '.join(map(str, matriz2[y2]))}")

    print("--------------Nueva Población--------------")
    for parejay in range(4):
        pareja1 = matriz2[parejay][0]
        pareja2 = matriz2[parejay][1]
        for x in range(corte, 11):  # rango
            matriz1[pareja1 - 1][x], matriz1[pareja2 - 1][x] = matriz1[pareja2 - 1][x], matriz1[pareja1 - 1][x]

    for y in range(8):
        binario1[y] = ''
        for x in range(11):  # rango
            binario1[y] += str(matriz1[y][x])

    for y1 in range(8):
        signo = -1 if matriz1[y1][0] == 1 else 1
        valor_absoluto = int(binario1[y1][1:-1], 2)
        valor = signo * valor_absoluto * (10 if matriz1[y1][-1] == 1 else 1)
        print(f"{y1 + 1}) {''.join(map(str, matriz1[y1]))} = {valor}")

    print("--------------Mutación--------------")
    xr = random.randint(1, 10)  # no se pone primer bit para mutracion 
    yr = random.randint(0, 7)  # ultimo bit se toma en cuenta para la mutacion 
    print("---La Mutación se hará en la posición [", yr, "]", "[", xr, "]")
    matriz1[yr][xr] = 1 if matriz1[yr][xr] == 0 else 0

    for y in range(8):
        binario1[y] = ''
        for x in range(11):  # rango
            binario1[y] += str(matriz1[y][x])

    signo = -1 if matriz1[0][0] == 1 else 1
    valor_absoluto = int(binario1[0][1:-1], 2)
    valor = signo * valor_absoluto * (10 if matriz1[0][-1] == 1 else 1)
    apto = [0, valor]

    for y1 in range(8):
        signo = -1 if matriz1[y1][0] == 1 else 1
        valor_absoluto = int(binario1[y1][1:-1], 2)
        valor = signo * valor_absoluto * (10 if matriz1[y1][-1] == 1 else 1)
        if valor > apto[1]:
            apto = [y1, valor]
        print(f"{y1 + 1}) {''.join(map(str, matriz1[y1]))} = {valor}")

    print("--------------Estudiante más apto--------------")
    print(apto[0] + 1, end=")")
    for ex in range(11):  # rango
        print(matriz1[apto[0]][ex], end="")
    print(" =", apto[1])

if __name__ == "__main__":
    main()
