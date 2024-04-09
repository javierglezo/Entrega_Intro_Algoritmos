""""Función que actúa de algoritmo para calcular el área del triángulo"""
def calcular_area_triangulo(base, altura):
    area = (0.5) * base * altura
    return area

def apartado_area_triangulo():
    base = float(input("Medida de la base: "))
    altura = float(input("Medida de la altura: "))
    area_triangulo = calcular_area_triangulo(base, altura)
    print("El área del triángulo es:", area_triangulo)

"""Respuesta apartado 2): podemos emplear este algoritmo solo que e vez de 
pasarle la medida de la altura y base, pasaríamos la de sus catetos perpendiculares."""
#Por lo tanto la respusta es SÍ solo que cambiando los nombres "base" y "altura" por "lado1" y "lado2":
def calcular_area_triangulo(lado1, lado2):
    area = (0.5) * lado1 * lado2
    return area

def apartado_area_tri_rectangulo():
    lado1 = float(input("Medida lado 1: "))
    lado2 = float(input("Medida lado 2: "))
    area_triangulo = calcular_area_triangulo(lado1, lado2)
    print("El área del triángulo es:", area_triangulo)


def mostrar_menu():
    print("1. Calcular área triángulo")
    print("2. Calcular área triámgulo rectángulo")
    print("3. Salir")

def main():
    while True:
        mostrar_menu()
        opcion = int(input("Seleccione apartado: "))
        print("Opción ingresada:", opcion)
        if opcion == 1:
            apartado_area_triangulo()
        elif opcion == 2:
            apartado_area_tri_rectangulo()
        elif opcion == 3:
            print("Gracias")
            break
        else:
            print("Opcion no valida")

main()

