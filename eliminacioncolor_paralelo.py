"""
eliminacion_color_paralelo.py

Este programa transforma una imagen a color en una imagen en blanco
y negro mediante una ejecución en paralelo de las operaciones.
Para ello, recibe un fichero en formato "ppm" tipo "ascii" y devuelve un
fichero en formato "pgm".

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
from multiprocessing import Array, Process
from time import time

class ImagenPpm:
    def __init__(self, Archivo: str):
        """
        Esta función inicializa una nueva instancia de la clase ImagenPpm.

        Args:
            Archivo (str): Ruta del archivo de imagen 'ppm' en fromato ascii.
        """
        self.Archivo = Archivo
        self.formato = None
        self.dim = None
        self.pixeles_RGB = [[], [], []]

    def Leer_archivo(self):
        '''
        Funcion que permite comprobar el numero magico P3 del archivo,
        almacena las dimensiones de la imagen y separa los píxeles en 
        tres canales de color: rojo, ver y azul.
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


def eliminar_color(array_gris: list, rojo: list, verde: list, azul: list,
                   ini: int, fin: int) -> None:
    """
    Esta función recibe tres listas de píxeles, realiza una operación de
    eliminación del color con los píxeles contenidos en sublistas de ellas,
    y añade los píxeles resultado a un array en memoria compartida.

    Args:
        array_gris (lis) Array en memoria compartida que contendrá
                         los píxeles sin color.
        rojo (list) Lista de valores de píxeles rojos.
        verde (list) Lista de valores de píxeles verdes.
        azul (list) Lista de valores de píxeles azules.
        ini (int) Inicio del rango de píxeles a los que eliminar el color.
        fin (int) Fin del rango de píxeles a los que eliminar el color.
    """

    # Eliminamos el color del píxel en posición i y lo añadimos a "array_gris".
    for i in range(ini, fin):
        pixel = (rojo[i] + verde[i] + azul[i]) // 3
        array_gris[i] = pixel


def elim_color_procesos(rojo: list, verde: list, azul: list, num_procesos:int,
                        len_imagen: int) -> list:
    """
    Esta función recibe tres listas de píxeles, las fragmenta en tantas 
    sublistas como número de procesos se le pasen a la función y aplica 
    sobre ellas la función de "eliminar_color". Los píxeles resultado de 
    cada proceso se almacenan en un array en memoria compartida.

    Args:
        rojo (list) Lista de valores de píxeles rojos.
        verde (list) Lista de valores de píxeles verdes.
        azul (list) Lista de valores de píxeles azules.
        num_procesos (int) Número de procesos que se van a usar en la 
                            paralelización.
        len_imagen (int) Total de píxeles o valores que conforman la imagen.
    """
     
    # Verificar que las listas tienen la misma longitud
    if len(rojo) != len(verde) or len(verde) != len(azul):
        # Esto, en función del resto de código, se puede redirigir a otra cosa
        raise ValueError("Las listas no tienen la misma longitud") 
    
    divisiones = len(rojo)//num_procesos
    resto = len(rojo) % num_procesos
    array_gris = Array("i", len_imagen, lock=False)

    # Creamos la lista de procesos.
    lista_procesos = list()
    for i in range(num_procesos):
        inicio = i*divisiones

        if i == num_procesos - 1:
            final = (i+1)*divisiones + resto 

        else:
            final = (i+1)*divisiones

        # En cada proceso se llama a la funcion que eliminar el color de un 
        # subconjunto de píxeles de cada lista.
        n = Process(target=eliminar_color, args=(array_gris, rojo, verde,
                                                 azul, inicio, final))
        lista_procesos.append(n)

    for proceso in lista_procesos:
        proceso.start()

    for proceso in lista_procesos:
        proceso.join()

    return (array_gris)


def grabar_imagen(ancho: int, alto: int, grises: list, filename: str) -> None:
    """
    Esta función recibe un alista de píxeles y, a partir de ella, graba una
    imagen en formato "pgm" con las dimensiones especificadas.

    Args:
        ancho (int) Ancho de la imagen en píxeles.
        alto (int) Alto de la imagen en píxeles.
        grises (list) Lista de valores de grises para los píxeles de la imagen.
        filename (str) Nombre del fichero pgm.
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
    a la función que eliminará el color de la imagen en paralelo y se graba el
    nuevo fichero obtenido. Se utiliza la función time() del módulo time para
    obtener el tiempo de ejecución empleado.
    """
    tiempo_inicial = time()

    # Creación del objeto Imagen_ppm
    Archivo = input("Por favor, introduce el nombre del archivo con"
                    " la extensión '.ppm': ")
    try:
        procesos = int(input("Introduzca el número de procesos que desea
                             " utilizar en la ejecución: "))
    except:
        print("El número de procesos no es reconocido, el programa se" 
              " ejecutará empleando 1 proceso.")
        procesos = 1

    imagen = ImagenPpm(Archivo)

    try:
        imagen.Leer_archivo()
    except ValueError:
        exit(1)

    # Eliminación del color
    long_array = imagen.dim[0]*imagen.dim[0]
    gris = elim_color_procesos(imagen.pixeles_RGB[0], imagen.pixeles_RGB[1],
                               imagen.pixeles_RGB[2], procesos, long_array)

    # Escribir el archivo en formato pgm
    nuevo_nombre = Archivo[:-3] + "pgm"

    grabar_imagen(imagen.dim[0], imagen.dim[1], gris, nuevo_nombre)

    tiempo_final = time()
    print("Tiempo de ejecución:", tiempo_final - tiempo_inicial)


if __name__ == "__main__":
    main()
