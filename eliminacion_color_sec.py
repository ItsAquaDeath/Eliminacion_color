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

class Imagen_ppm:
    ''' 
    Lee y carga una imagen en formato ppm tipo Ascii comprobando formato.

    Args:
        Archivo_ppm (str): Ruta del archivo de imagen en formato .ppm
    '''

    def __init__(self, Archivo_ppm: str):
        self.Archivo_ppm = Archivo_ppm
        self.formato = None
        self.dimensiones = None
        self.pixeles_RGB = [[],[],[]]

    def Leer_archivo(self):
        ''' 
        Funcion que permite comprobar el numero magico P3 del archivo,
        muestra las dimensiones de la imagen
        '''
        with open(self.Archivo_ppm, 'r') as archivo:
            lineas = archivo.readlines()
            if lineas[0].strip() != 'P3':
                raise ValueError("Formato de archivo PPM incorrecto")
            self.dimensiones = tuple(map(int, lineas[1].split()))
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


def eliminar_color(rojo, verde, azul):
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


def main():
    imagen = Imagen_ppm('CuestionarioGrupo02.EliminacionColor.lenaoriginal.ppm')
    try:
        imagen.Leer_archivo()
    except ValueError:
        exit 1

    print(f"Formato: {imagen.formato}")
    print(f"Dimensiones: {imagen.dimensiones}")
    print(imagen.pixeles_RGB) 

    
if __name__ == "__main__":
    main()

