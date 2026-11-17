def rut_valido(rut):
    """
    Valida rut verificador utilizando metodo 11 

    La funcion se le ingresa el rut con o sin puntos y con guion,
    y luego verifica si el rut dado es correcto o no como true or false y acepta k o K
    """

    numeros, verificador = rut.replace(".","").split("-")
    numero_invertido = numeros[::-1]
    total = 0
    multiplicador = 2
    for numero in numero_invertido:
        total += int(numero) * multiplicador 
        multiplicador +=1
        if multiplicador > 7:
            multiplicador = 2
    resto = total % 11 
    numero_calculado = 11- resto
    if numero_calculado == 11:
        numero_calculado = '0'
    elif numero_calculado == 10:
        numero_calculado ='K'
    else:
        numero_calculado = str(numero_calculado)

    return numero_calculado == verificador.upper()

print(rut_valido("12.345.678-5"))   # True
print(rut_valido("12.345.678-9"))   # False
print(rut_valido("12345678-5"))     # True
print(rut_valido("10.000.013-K"))   # True
print(rut_valido("10.000.013-k"))   # True