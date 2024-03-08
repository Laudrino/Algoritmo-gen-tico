import random

def main():
    # Genera una matriz de 8 filas y 11 columnas, con valores aleatorios 0 o 1
    matriz1 = [[random.randint(0, 1) for _ in range(11)] for _ in range(8)] # poblacion inical 
    # Crea una matriz de 4 filas y 2 columnas llena de ceros
    matriz2 = [[0, 0] for _ in range(4)]
    # Inicializa una lista para almacenar los valores decimales de los binarios
    apto = [0, 0]
    # Inicializa una lista de cadenas vacías para almacenar los binarios
    binario1 = ['' for _ in range(8)]
    # Inicializa variables adicionales
    num = 0
    corte = 0

    # Convierte cada fila de la matriz1 en una cadena binaria y la almacena en binario1
    for y in range(8):
        binario1[y] = ''
        for x in range(11):  # rango 
            binario1[y] += str(matriz1[y][x])

    print("--------------Población Inicial--------------")
    # Muestra la población inicial junto con su valor decimal correspondiente
    for y1 in range(8):
        signo = -1 if matriz1[y1][0] == 1 else 1
        valor_absoluto = int(binario1[y1][1:-1], 2)
        valor = signo * valor_absoluto * (10 if matriz1[y1][-1] == 1 else 1)  # bit para decimal y no decimal
        print(f"{y1 + 1}) {''.join(map(str, matriz1[y1]))} = {valor}")

    while True:
        try:
            # Solicita al usuario un número entre 1 y 6 para determinar la posicion del corte, el punto de corte determina dónde se realizará este cruce en las cadenas binarias que representan a los individuos
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
    # Muestra las parejas de población para el cruce
    matriz2 = [[8, 2], [6, 1], [5, 3], [7, 4]]
    for y2 in range(4):
        print(f"{y2 + 1}) {' '.join(map(str, matriz2[y2]))}")

    print("--------------Nueva Población--------------")
    # Realiza el cruce de las parejas seleccionadas
    for parejay in range(4):
        pareja1 = matriz2[parejay][0]
        pareja2 = matriz2[parejay][1]
        for x in range(corte, 11):  # rango
            matriz1[pareja1 - 1][x], matriz1[pareja2 - 1][x] = matriz1[pareja2 - 1][x], matriz1[pareja1 - 1][x]

    # Convierte cada fila de la matriz1 en una cadena binaria y la almacena en binario1
    for y in range(8):
        binario1[y] = ''
        for x in range(11):  # rango
            binario1[y] += str(matriz1[y][x])

    # Muestra la nueva población junto con su valor decimal correspondiente
    for y1 in range(8):
        signo = -1 if matriz1[y1][0] == 1 else 1
        valor_absoluto = int(binario1[y1][1:-1], 2)
        valor = signo * valor_absoluto * (10 if matriz1[y1][-1] == 1 else 1)
        print(f"{y1 + 1}) {''.join(map(str, matriz1[y1]))} = {valor}")

    print("--------------Mutación--------------")
    # Realiza una mutación aleatoria en la población
    xr = random.randint(1, 10)  # no se pone primer bit para mutracion 
    yr = random.randint(0, 7)  # ultimo bit se toma en cuenta para la mutacion 
    print("---La Mutación se hará en la posición [", yr, "]", "[", xr, "]")
    matriz1[yr][xr] = 1 if matriz1[yr][xr] == 0 else 0

    # Convierte cada fila de la matriz1 en una cadena binaria y la almacena en binario1
    for y in range(8):
        binario1[y] = ''
        for x in range(11):  # rango
            binario1[y] += str(matriz1[y][x])

    # Calcula el valor decimal del primer individuo en la población mutada
    signo = -1 if matriz1[0][0] == 1 else 1
    valor_absoluto = int(binario1[0][1:-1], 2)
    valor = signo * valor_absoluto * (10 if matriz1[0][-1] == 1 else 1)
    apto = [0, valor]

    # Muestra la población mutada junto con su valor decimal correspondiente
    for y1 in range(8):
        signo = -1 if matriz1[y1][0] == 1 else 1
        valor_absoluto = int(binario1[y1][1:-1], 2)
        valor = signo * valor_absoluto * (10 if matriz1[y1][-1] == 1 else 1)
        if valor > apto[1]:
            apto = [y1, valor]
        print(f"{y1 + 1}) {''.join(map(str, matriz1[y1]))} = {valor}")

    print("--------------Estudiante más apto--------------")
    # Muestra al individuo más apto de la población mutada
    print(apto[0] + 1, end=")")
    for ex in range(11):  # rango
        print(matriz1[apto[0]][ex], end="")
    print(" =", apto[1])

if __name__ == "__main__":
    main()
