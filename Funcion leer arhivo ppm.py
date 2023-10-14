
# Funcion leer archivo "ppm"

def leer_ppm_file(filename):
    ppm_dato = None
    # Asegurar que sea el formato correct 
    with open(filename, 'r') as file:
        magic_number = file.readline().strip()


        if magic_number != "P3":
            print("Error: no es un archivo PPM.")
            return None
        # leer datos
        ancho, altura = map(int, file.readline().split())
        rojo = []
        azul = []
        verde = []
        
        for line in file:
            valores = list(map(int, line.strip().split()))
            for i in range(0, len(valores), 3):
                rojo.append(valores[i])
                if i + 1 < len(valores):
                    verde.append(valores[i + 1])
                if i + 2 < len(valores):
                    azul.append(valores[i + 2])
        
        # Guardar datos en ppm_dato
        ppm_dato = magic_number, ancho, altura, rojo, azul, verde
    
    return ppm_dato

# Llamada a la función y mostrar resultados
filename = "CuestionarioGrupo02.EliminacionColor.lenaoriginal.ppm"
ppm_dato = leer_ppm_file(filename)


# Mostrar resultados
if ppm_dato is not None:
    magic_number, ancho, altura, rojo, verde, azul = ppm_dato
    print(f"Número Mágico: {magic_number}")
    print(f"Ancho: {ancho}")
    print(f"Altura: {altura}")
    print(rojo)