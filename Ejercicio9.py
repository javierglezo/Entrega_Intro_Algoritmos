"""Función que actúa de algoritmo para calcular la media"""
def calcular_media(n1, n2, n3):
    media_aritmetica = (n1 + n2 + n3) / 3
    return media_aritmetica

def apartado_media():
    n_1 = float(input("Ingrese el primer número: "))
    n_2 = float(input("Ingrese el segundo número: "))
    n_3 = float(input("Ingrese el tercer número: "))
    media = calcular_media(n_1, n_2, n_3)
    print("La media aritmética es:", media)


"""Función que actúa de algoritmo para calcular la media con coeficientes de ponderación"""
def calcular_media_ponderada(n1, n2, n3, p1, p2, p3):
    media_ponderada = (n1 * p1 + n2 * p2 + n3 * p3) / (p1 + p2 + p3)
    return media_ponderada

def apartado_media_ponderada():
    n1 = float(input("Ingrese el primer número: "))
    n2 = float(input("Ingrese el segundo número: "))
    n3 = float(input("Ingrese el tercer número: "))
    p1 = float(input("Ingrese el primer coeficiente de ponderación: "))
    p2 = float(input("Ingrese el segundo coeficiente de ponderación: "))
    p3 = float(input("Ingrese el tercer coeficiente de ponderación: "))
    media = calcular_media_ponderada(n1, n2, n3, p1, p2, p3)
    print("La media ponderada es:", media)

def mostrar_menu():
    print("1. Calcular media")
    print("2. Calcular media ponderada")
    print("3. Salir")

def main():
    while True:
        mostrar_menu()
        opcion = int(input("Seleccione apartado: "))
        print("Opción ingresada:", opcion)
        if opcion == 1:
            apartado_media()
        elif opcion == 2:
            apartado_media_ponderada()
        elif opcion == 3:
            print("Gracias")
            break
        else:
            print("Opcion no valida")

main()

