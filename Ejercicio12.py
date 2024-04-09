class CUENTA:
    def __init__(self, titular, saldo_inicial=0, limite_descubierto=0):
        self.titular = titular
        self.saldo = saldo_inicial
        self.limite_descubierto = limite_descubierto
    
    def depositar(self, suma):
        if suma > 0:
            self.saldo += suma
            print(f"Depósito realizado: {suma}. Saldo actual: {self.saldo}")
        else:
            print("El dinero a dejar debe ser positivo.")
    
    def retirar(self, suma):
        if suma <= self.saldo + self.limite_descubierto:
            self.saldo -= suma
            print(f"Retiro realizado: {suma}. Saldo actual: {self.saldo}")
        else:
            print("Fondos insuficientes para completar el retiro.")

def obtener_valor_positivo(mensaje):
    while True:
        valor = float(input(mensaje))
        if valor >= 0:
            return valor
        else:
            print("Por favor, introduce un valor positivo.")

def obtener_accion_usuario():
    while True:
        accion = input("¿Deseas depositar o retirar dinero? (depositar/retirar): ").lower()
        if accion in ["depositar", "retirar"]:
            return accion
        else:
            print("Por favor, escribe 'depositar' o 'retirar' para seleccionar tu acción.")

titular = input("Introduce el nombre del titular de la cuenta: ")
saldo_inicial = obtener_valor_positivo("Introduce el saldo inicial de la cuenta: ")
limite_descubierto = obtener_valor_positivo("Introduce el límite de descubierto autorizado: ")
cuenta_usuario = CUENTA(titular, saldo_inicial, limite_descubierto) #Instancia
accion_usuario = obtener_accion_usuario()
suma = obtener_valor_positivo("Introduce la suma: ")
if accion_usuario == "depositar":
    cuenta_usuario.depositar(suma)
elif accion_usuario == "retirar":
    cuenta_usuario.retirar(suma)
print(f"Saldo final en la cuenta de {cuenta_usuario.titular}: {cuenta_usuario.saldo}")
