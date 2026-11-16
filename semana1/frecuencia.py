#1. Separar la frase en palabras.
#2. Preparar una tabla vacía de palabra -> cantidad.
#3. Leer las palabras una por una:
  # - si ya está en la tabla, sumarle 1
 #  - si no está, anotarla con 1
#. Ordenar la tabla de mayor a menor cantidad.
#5. Quedarme con las 3 primeras.


def contador_de_palabras(texto):
    """
    Contador de palabras que separa estas mismas y devuelve las 3 primeras de mayor a menor
    """
    cantidad = {}
    for palabra in texto.lower().split():
        if palabra in cantidad :
            cantidad[palabra] += 1
        else:
            cantidad[palabra] = 1 
    return sorted(cantidad.items(), key=lambda par: par[1], reverse=True)[:3]


print(contador_de_palabras("texto de prueba texto de prueba texto para pruebas texto con pruebas"))
print(contador_de_palabras("el gato"))
print(contador_de_palabras("el perro"))

# from collections import Counter

# def contador_de_palabras2(texto):
#     """Devuelve las 3 palabras mas repetidas del texto con su cantidad version rapida."""
#     return Counter(texto.lower().split()).most_common(3)


# print(contador_de_palabras("texto de prueba texto de prueba texto para pruebas texto con pruebas"))
# print(contador_de_palabras("el gato"))
# print(contador_de_palabras("el perro"))
