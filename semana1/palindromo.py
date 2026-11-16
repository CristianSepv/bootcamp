tildes = {"á":"a","é":"e","í":"i","ó":"o","ú":"u"}

def es_palindromo(texto):
    """
    Este Ejercicio es un palidromo simple , devulve true si el texto se lee igual al derecho y al revez y 
    se le omiten comas, mayusculas y tildes
    """
    texto_base = texto.lower().replace(" ","")
    for con_tilde, sin_tilde in tildes.items():
        texto_base= texto_base.replace(con_tilde, sin_tilde)

    texto_inverso = texto_base[::-1]
    return texto_base == texto_inverso
    

print(es_palindromo("oso"))                 # deberia dar True
print(es_palindromo("Sé verlas al revés"))  # deberia dar True
print(es_palindromo("Python"))