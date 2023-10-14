def pgm(ancho: int, alto: int, grises: list) -> str:
    """
    Genera una imagen PGM en formato P2 con las dimensiones especificadas y una
    lista de valores de grises.

    Args:
        ancho (int) Ancho de la imagen en píxeles.
        alto (int) Alto de la imagen en píxeles.
        grises (list) Lista de valores de grises para los píxeles de la imagen.

    Returns:
        (str) Una cadena que contiene el contenido de la imagen PGM en formato
              P2.
    """

    n = len(grises)
    magico = 'P2'
    max_color = '255'
    dim = str(ancho) + ' ' + str(alto)

    contenido = [magico, dim, max_color]
    contenido = '\n'.join(contenido)
    contenido += '\n'

    for i in range(n):
        if (i + 1) % ancho == 0:
            contenido += str(grises[i]) + '\n'
        else:
            contenido += str(grises[i]) + ' '

    return contenido


def main():

    nombre_archivo = "CuestionarioGrupo02.EliminacionColor.lenaoriginal.ppm"
    nombre_archivo = nombre_archivo.split('.')[:-2]
    nombre_archivo = '.'.join(nombre_archivo)

    lista_prueba = [1]*36
    alto = 6
    ancho = 6
    imagen = pgm(ancho, alto, lista_prueba)

    out = open(nombre_archivo+'.lenagris.pgm', 'w')
    out.write(imagen)


if __name__ == '__main__':
    main()

