def validar_rut(rut: str) -> bool:
    """
        Valida rut verificador utilizando modulo 11 
    
        Recibe un rut con o sin puntos y con guion,
        y luego verifica si el rut dado es correcto o no como true/false y acepta k o K
    """
    if not isinstance(rut, str):
        raise TypeError("El rut debe ser un string")
    if rut.count("-") != 1:
        return False

    rut_base, verificador = rut.replace(".", "").upper().split("-")
    if not rut_base.isdigit() or len(verificador) != 1 or verificador not in "0123456789K":
        return False
    
    multiplicador = 2
    rut_suma = 0
    for numero in rut_base[::-1]:
        rut_total = int(numero) * multiplicador
        rut_suma += rut_total
        multiplicador += 1
        if multiplicador > 7:
            multiplicador = 2
    resto = rut_suma % 11
    verificacion = 11 - resto

    if verificacion == 11:
        rut_verificacion = "0"
    elif verificacion == 10:
        rut_verificacion = "K"
    else:
        rut_verificacion = str(verificacion)

    return rut_verificacion == verificador

    
print(validar_rut("12.345.678-5"))
print(validar_rut("12345678-5"))
print(validar_rut("123456785"))  # False: falta el guion
print(validar_rut("12345678-9"))
print(validar_rut("10000013-K"))  # True
print(validar_rut("10000013-k"))  # True: minúscula
print(validar_rut("10000004-0"))  # True
print(validar_rut("10000004-K"))  # False
print(validar_rut(123456788))