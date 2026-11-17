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