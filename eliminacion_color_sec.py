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
    Lee y carga una imagen en formato ppm tipo Ascii comprobando formato,
    como entrada requiere ruta de archivo de imagen en formato .ppm 
    metodo de la clase pixeles_RGB contiene lista de de los pixeles para 
    color 
    '''

    def __init__(self, Archivo_ppm):
        self.Archivo_ppm = Archivo_ppm
        self.formato = None
        self.dimensiones = None
        self.pixeles_RGB = [[],[],[]]

    def Leer_archivo(self):
        ''' 
        Funcion que permite comprobar el  numero magico P3 del archivo,
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

def main():
    imagen = Imagen_ppm('CuestionarioGrupo02.EliminacionColor.lenaoriginal.ppm')
    imagen.Leer_archivo()

    print(f"Formato: {imagen.formato}")
    print(f"Dimensiones: {imagen.dimensiones}")
    print(imagen.pixeles_RGB) 

if __name__ == "__main__":
    main()