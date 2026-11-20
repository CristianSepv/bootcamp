class CuentaBancaria:
    """
        Cuenta con saldo que permite depositar, retirar y consultar dinero.
 
        El saldo parte en 0.
    """

    def __init__(self):
        self._saldo = 0

    def depositar(self,monto):  
        """ 
            Deposita monto a saldo 

            lanza error si monto es menor igual a cero
        """
        if monto <= 0:
            raise ValueError("El monto debe ser positivo mayor a cero")
        self._saldo += monto
        
    def retirar(self,monto):
        """
            Resta el monto del saldo.
        
            Lanza ValueError si el monto es menor o igual a 0
            o si supera el saldo disponible.
        """
        if monto <= 0:
            raise ValueError("El monto debe ser positivo mayor a cero")
        if monto > self._saldo:
            raise ValueError("El monto no debe superar al saldo")
        self._saldo -= monto

    def guardar(self,ruta):
        """
            Guarda el monto el saldo actual en el archivo indicado
        """
        with open(ruta,"w" ,encoding="utf-8") as archivo:
            guardado = str(self._saldo)
            archivo.write(guardado)

    def cargar(self, ruta):
        """
            Carga archivo guardado y si el archivo no existe vuelve saldo a 0
        """
        try:
            with open(ruta,"r" ,encoding="utf-8") as archivo:
                self._saldo = int(archivo.read())
        except FileNotFoundError :
            self._saldo = 0

    def registrar(self,ruta,tipo,monto):
        """
            Registra si se deposita o retira dinero y crea el archivo si es que no exite,
            si existe registra los cambios
        """
        with open(ruta , "a", encoding="utf-8") as archivo:
            linea = f"{tipo},{monto}\n"
            archivo.write(linea)

    def leer_movimientos(self, ruta):
        """
            Lee los movimientos del archivo registrado y los muestra de manera ordenada
        """
        movimientos = []
        with open(ruta , "r", encoding="utf-8")as archivo:
            for linea in archivo:
                tipo, monto = linea.strip().split(",")
                movimientos.append((tipo, int(monto)))
        return movimientos

    def ver_saldo(self):
        """Devuelve el saldo actual."""
        return self._saldo

#Pruebas funcionanmiento archivos
cuenta = CuentaBancaria()
cuenta.depositar(5000)
cuenta.guardar("saldo.txt")

nueva = CuentaBancaria()
nueva.cargar("saldo.txt")
print(nueva.ver_saldo()) 
otra = CuentaBancaria()
otra.cargar("no_existe.txt")
print(otra.ver_saldo())   # 0, sin error

cuenta = CuentaBancaria()
cuenta.depositar(5000)
cuenta.registrar("movimientos.txt", "deposito", 5000)
cuenta.retirar(3000)
cuenta.registrar("movimientos.txt", "retiro", 3000)

movimientos = cuenta.leer_movimientos("movimientos.txt")
for tipo, monto in movimientos:
    print(f"{tipo}: ${monto}")


#Pruebas depositar retirar 
cuenta = CuentaBancaria()
cuenta.depositar(5000)
cuenta.retirar(3000)
print(cuenta.ver_saldo())    

otra = CuentaBancaria()
print(otra.ver_saldo())     

#Pruebas try expect
try:
    cuenta.retirar(50000)
except ValueError as error:
    print("No se pudo retirar:", error)

print("El programa sigue funcionando")