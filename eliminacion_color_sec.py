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


class ImagenPpm:
    ''' 
    Lee y carga una imagen en formato ppm tipo Ascii comprobando formato.

    Args:
        Archivo_ppm (str): Ruta del archivo de imagen en formato .ppm
    '''

    def __init__(self, Archivo: str):
        self.Archivo = Archivo
        self.formato = None
        self.dim = None
        self.pixeles_RGB = [[],[],[]]

    def Leer_archivo(self):
        ''' 
        Funcion que permite comprobar el numero magico P3 del archivo,
        muestra las dimensiones de la imagen
        '''
        with open(self.Archivo, 'r', encoding="utf-8") as archivo:
            lineas = archivo.readlines()
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
    # Verificar que las listas tienen la misma longitud
    if len(rojo) != len(verde) or len(verde) != len(azul):
        # Esto, en función del resto de código, se puede redirigir a otra cosa
        raise ValueError("Las listas no tienen la misma longitud") 
             
    # Lista de resultados de grises
    grises = []

    # Iterar sobre las listas y obtener el valor de gris para cada pixel
    for i in range(len(rojo)):
        pixel = (rojo[i] + verde[i] + azul[i]) // 3
        grises.append(pixel)

    return grises


def grabar_imagen(ancho: int, alto: int, grises: list, filename: str) -> None:
    """
    Graba una imagen en formato PGM con las dimensiones especificadas y una
    lista de valores de grises.

    Args:
        ancho (int): Ancho de la imagen en píxeles.
        alto (int): Alto de la imagen en píxeles.
        grises (list): Lista de valores de grises para los píxeles de la 
                       imagen.
        filename (str): Nombre del fichero pgm
    """

    # Se abre el fichero y se escribe la cabecera
    f_out = open(filename, "a", encoding="utf-8")
    f_out.write("P2\n")
    f_out.write("255\n")
    f_out.write(str(ancho) + " " + str(alto))

    # Se escribe el contenido de la imagen en escala de grises
    linea = ""
    for i in range(len(grises)):
        if i % ancho == 0:
            f_out.write(linea)
            linea = "\n" + str(grises[i]) + " "
        else:
            linea += str(grises[i]) + " "

    f_out.write("\n")
    # Se cierra el gestor de fichero
    f_out.close()
   

def main():
    """
    Programa principal.
    """
    # Creación del objeto Imagen_ppm
    ARCHIVO = 'CuestionarioGrupo02.EliminacionColor.lenaoriginal.ppm'
    imagen = ImagenPpm(ARCHIVO)
    try:
        imagen.Leer_archivo()
    except ValueError:
        exit(1)

    # Eliminación del color
    gris = eliminar_color(imagen.pixeles_RGB[0], imagen.pixeles_RGB[1],
                          imagen.pixeles_RGB[2])

    # Escribir el archivo en formato pgm
    nuevo_nombre = ARCHIVO[:-3] + "pgm"

    grabar_imagen(imagen.dim[0], imagen.dim[1], gris, nuevo_nombre)


if __name__ == "__main__":
    main()
