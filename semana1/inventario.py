# 1. Crear la funcion
# 2. Preparar total en 0 y una lista vacia de sin_stock
# 3. Recorrer los productos con un for
# 4. En cada vuelta: multiplicar precio por stock y sumarlo al total
# 5. Si el stock es 0, agregar el nombre a sin_stock
# 6. Retornar total y sin_stock

def resumen_inventario(productos):
    """
    Calcula el valor total de lo productos totales

    multiplica sus productos por la cantidad de stock en inventario y lo deja todo en una variable total, tambien
    guarda el nombre de los productos que no tienen stock
    """
    total = 0
    sin_stock = []
    for producto in productos:
        total += producto["precio"] * producto["stock"]
        if producto["stock"] == 0:
            sin_stock.append(producto["nombre"])

    return  total, sin_stock

    


productos = [
    {"nombre": "teclado", "precio": 15000, "stock": 4},
    {"nombre": "mouse", "precio": 8000, "stock": 0},
    {"nombre": "monitor", "precio": 90000, "stock": 2},
]

total, sin_stock = resumen_inventario(productos)   # recibir
print("Valor total:", total)                       # mostrar
print("Sin stock:", sin_stock)