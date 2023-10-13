"""
eliminacion_color_sec.py

Una descripción muy buena de lo que hace el programa :D

Trabajos de Programación avanzada: Trabajo grupal 1

Versión: 1.0
Autores: xxxx
         xxxxxxxxxxxxxxxx
         xxxxxxxxxxxxxxx
         xxxxx
         xxxxxxx

Fecha DD/MM/YYYY
"""
def eliminar_color(rojo, verde, azul):
    # Verificar que las listas tienen la misma longitud
    if len(rojo) != len(verde) or len(verde) != len(azul):
        # Esto, en función del resto de código, se puede redirigir a otra cosa
        raise ValueError("Las listas no tienen la misma longitud") 
             
    # Lista de resultados de grises
    grises = []

    # Iterar sobre las listas y obtener el valor de gris para caada pixel
    for i in range(len(rojo)):
        pixel = (rojo[i] + verde[i] + azul[i]) // 3
        grises.append(pixel)

    return grises
