"""
eliminacion_color_sec.py

Este programa secuencial transforma una imagen a color en una imagen en blanco
y negro. Para ello, recibe un fichero en formato "ppm" tipo "ascii"
y devuelve un fichero en formato "pgm".

Trabajos de Programación avanzada.
Cuestionarios en grupo 1: Eliminación del color.

Versión: 1.0
Autores: Ana García Gambín
         Alvaro Martínez MArtínez
         Laura Tur Giménez
         Nidia Nathalia Vega Romero
         Qinding Xie

Fecha 20/01/2024
"""
from time import time


class ImagenPpm:
    def __init__(self, Archivo: str):
        """
        Esta función inicializa una nueva instancia de la clase ImagenPpm.

        Args:
            Archivo (str): Ruta del archivo de imagen en formato .ppm
        """
        self.Archivo = Archivo
        self.formato = None
        self.dim = None
        self.pixeles_RGB = [[], [], []]

    def Leer_archivo(self):
        '''
        Funcion que permite comprobar el numero magico P3 del archivo,
        almacena las dimensiones de la imagen y separa los píxeles en
        tres canales de color: rojo, verde y azul.
        '''
        try:
            archivo = open(self.Archivo, 'r', encoding="utf-8")
        except FileNotFoundError:
            raise FileNotFoundError("Archivo %s no encontrado!" % self.Archivo)
        lineas = archivo.readlines()
        archivo.close()
        if lineas[0].strip() != 'P3':
            raise ValueError("Formato de archivo PPM incorrecto")

        self.dim = tuple(map(int, lineas[1].split()))
        datos = [list(map(int, linea.split())) for linea in lineas[3:]]
        R = []
        G = []
        B = []
        for fila in datos:
            for i in range(0, len(fila), 3):
                R.append(fila[i])
                G.append(fila[i+1])
                B.append(fila[i+2])
        self.pixeles_RGB = [R, G, B]


def eliminar_color(rojo: list, verde: list, azul: list) -> list:
    """
    Esta función recibe tres listas de píxeles y devuelve una lista con los
    píxeles resultado tras la operación de eliminación del color.

    Args:
        rojo (list) Lista de valores de píxeles rojos.
        verde (list) Lista de valores de píxeles verdes.
        azul (list) Lista de valores de píxeles azules.

    Returns:
        grises (list) Lista de valores de píxeles sin color.
    """
    # Verificar que las listas tienen la misma longitud
    if len(rojo) != len(verde) or len(verde) != len(azul):
        raise ValueError("Las listas no tienen la misma longitud")

    grises = []

    # Iterar sobre las listas y obtener el valor de gris para cada pixel
    for i in range(len(rojo)):
        pixel = (rojo[i] + verde[i] + azul[i]) // 3
        grises.append(pixel)

    return grises


def grabar_imagen(ancho: int, alto: int, grises: list, filename: str) -> None:
    """
    Esta función recibe un alista de píxeles y, a partir de ella, graba una
    imagen en formato "pgm" con las dimensiones especificadas.

    Args:
        ancho (int) Ancho de la imagen en píxeles.
        alto (int) Alto de la imagen en píxeles.
        grises (list) Lista de valores de grises para los píxeles de la imagen.
        filename (str) Nombre del fichero pgm
    """

    # Se abre el fichero y se escribe la cabecera
    f_out = open(filename, "a", encoding="utf-8")
    f_out.write("P2\n")
    f_out.write(str(ancho) + " " + str(alto) + "\n")
    f_out.write("255")

    # Se escribe el contenido de la imagen en escala de grises
    linea = ""
    for i in range(len(grises)):
        if i % ancho == 0:
            f_out.write(linea)
            linea = "\n" + str(grises[i]) + " "
        else:
            linea += str(grises[i]) + " "

    f_out.write(linea + "\n")
    # Se cierra el gestor de fichero
    f_out.close()


def main():
    """
    Función correspondiente al programa principal. Se pide el nombre de la
    imagen al usuario para, a continuación, crear la clase ImagenPpm. Se llama
    a la función que eliminará el color de la imagen y se graba el nuevo
    fichero obtenido. Se utiliza la función time() del módulo time para obtener
    el tiempo de ejecución empleado.
    """
    print("Este programa permite eliminar la información de color contenida "
          "en una imagen 'ppm' tipo 'ascii'.")

    # Creación del objeto Imagen_ppm
    Archivo = input("Por favor, introduce el nombre del archivo con"
                    " la extensión '.ppm': ")
    tiempo_inicial = time()

    imagen = ImagenPpm(Archivo)

    try:
        imagen.Leer_archivo()
    except ValueError as e:
        print(e)
        exit(1)
    except FileNotFoundError as e:
        print(e)
        exit(1)

    # Eliminación del color
    gris = eliminar_color(imagen.pixeles_RGB[0], imagen.pixeles_RGB[1],
                          imagen.pixeles_RGB[2])

    # Escribir el archivo en formato pgm
    nuevo_nombre = Archivo[:-3] + "pgm"

    grabar_imagen(imagen.dim[0], imagen.dim[1], gris, nuevo_nombre)

    tiempo_final = time()
    print("¡Ejecución finalizada! La imagen sin color se ha guardado en el "
          "fichero %s." % nuevo_nombre)
    print("El programa ha tardado %.4f segundos en su ejecución."
          % (tiempo_final - tiempo_inicial))


if __name__ == "__main__":
    main()
