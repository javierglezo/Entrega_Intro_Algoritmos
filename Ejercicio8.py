"""Función que actúa de algoritmo para calcular el precio final de un producto añadiendo el IVA, 
utilizando dos parámetros a ingresar ("precio_sin_iva" y "porcentaje_iva")"""
def calcular_precio_con_iva(precio_sin_iva, porcentaje_iva):
    iva = precio_sin_iva * (porcentaje_iva / 100)
    precio_con_iva = precio_sin_iva + iva
    return precio_con_iva


def apartado_iva():
    precio_sin_iva = float(input("Ingrese el precio sin impuestos: "))
    porcentaje_iva = float(input("Ingrese el porcentaje de IVA: "))
    precio_total = calcular_precio_con_iva(precio_sin_iva, porcentaje_iva)
    print(f"El precio con iva añadido es: {precio_total} $")


"""Función que actúa como algoritmo para calcular el interes"""
def calcular_intereses_inversion(capital_invertido, tasa_interes_mensual, tiempo_meses):
    intereses_generados = capital_invertido * tasa_interes_mensual * tiempo_meses
    return intereses_generados

def apartado_interes():
    capital_invertido = float(input("Ingrese el capital invertido: "))
    tasa_interes_mensual = float(input("Ingrese la tasa de interés mensual (%): ")) / 100
    tiempo_meses = int(input("Ingrese el tiempo en meses: "))
    intereses = calcular_intereses_inversion(capital_invertido, tasa_interes_mensual, tiempo_meses)
    print("Los intereses generados son:", intereses)

def mostrar_menu():
    print("1. Calcular precio con IVA")
    print("2. Calcular intereses")
    print("3. Salir")

def main():
    while True:
        mostrar_menu()
        opcion = int(input("Seleccione apartado: "))
        print("Opción ingresada:", opcion)
        if opcion == 1:
            apartado_iva()
        elif opcion == 2:
            apartado_interes()
        elif opcion == 3:
            print("Gracias")
            break
        else:
            print("Opcion no valida")

main()