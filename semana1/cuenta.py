class CuentaBancaria:
    """Cuenta con saldo que permite depositar, retirar y consultar dinero.

    El saldo parte en 0.
    """

    def __init__(self):
        self._saldo = 0


    def depositar(self,monto):  
        if monto <= 0:
            raise ValueError("El monto debe ser positivo mayor a cero")
        self._saldo += monto
        """Resta el monto del saldo.

        Lanza ValueError si el monto es menor o igual a 0
        o si supera el saldo disponible.
        """

    def retirar(self,monto):
        if monto <= 0:
            raise ValueError("El monto debe ser positivo mayor a cero")
        if monto > self._saldo:
            raise ValueError("El monto no debe superar al saldo")
        self._saldo -= monto

    """Resta el monto del saldo.

        Lanza ValueError si el monto es menor o igual a 0
        o si supera el saldo disponible.
        """

    def saldo(self):
        return self._saldo
    """Devuelve el saldo actual."""
    
cuenta = CuentaBancaria()
cuenta.depositar(5000)
cuenta.retirar(3000)
print(cuenta.saldo())    

otra = CuentaBancaria()
print(otra.saldo())     

try:
    cuenta.retirar(50000)
except ValueError as error:
    print("No se pudo retirar:", error)

print("El programa sigue funcionando")