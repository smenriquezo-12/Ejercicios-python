import math


def area_circulo(radio, redondear=False, decimales=2):
    """Calcula el área de un círculo dado su radio.

    Parámetros:
    radio (float): El radio del círculo. Debe ser mayor o igual a cero.
    redondear (bool): Si es True, redondea el resultado a `decimales` cifras.
    decimales (int): Cantidad de decimales para redondear cuando `redondear` es True.

    Retorna:
    float: El área del círculo (pi * radio^2), o su versión redondeada si se solicita.

    Lanza:
    ValueError: Si el radio es negativo.
    """
    if radio < 0:
        raise ValueError("El radio no puede ser negativo")

    area = math.pi * radio ** 2
    return round(area, decimales) if redondear else area
