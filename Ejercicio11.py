def calcular_horas_extra(salario_mensual_bruto, horas_extra_trabajadas):
    horas_normales_por_mes = 35 * 4  
    tarifa_hora_normal = salario_mensual_bruto / horas_normales_por_mes / 35  
    if horas_extra_trabajadas <= 7:
        return 0  
    elif 8 <= horas_extra_trabajadas <= 43:
        tarifa_hora_extra = tarifa_hora_normal * 1.25
    else:
        tarifa_hora_extra = tarifa_hora_normal * 1.5
    horas_extra_pagadas = (horas_extra_trabajadas - 7) * tarifa_hora_extra
    return horas_extra_pagadas

def main():
    salario_mensual_bruto = float(input("Ingrese el salario mensual bruto: "))
    horas_extra_trabajadas = int(input("Ingrese la cantidad de horas extra trabajadas en el mes: "))
    importe_horas_extra = calcular_horas_extra(salario_mensual_bruto, horas_extra_trabajadas)
    print("El importe de las horas extra que hay que pagar es:", importe_horas_extra)

main()