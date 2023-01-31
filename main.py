from discretizar import discretizacion
from bfs import BFS

def numEnt():
    correcto = False
    num = 0
    while (correcto != True):
        try:
            num = int(input("Ingrese el numero de algoritmo deseado: "))
            correcto = True
        except ValueError:
            print("No ingreso un numero")
    return num

salir = False
opcion = 0

while (salir != True):
  print("*** Bienvenido a Maze Solver ***")
  print("1. BFS")
  print("2. DFS")
  print("3. Djikstra")
  print("4. Salir")

  opcion = numEnt()

  if opcion == 1:
    print('BFS\n')
    archivo = input("Ingrese el nombre del archivo con su extencion: ")
    discretizacion(archivo)
    nuevo_archivo = "resultado_" + archivo
    BFS(nuevo_archivo)
       
  elif opcion == 2:
    print('DFS\n')

  elif opcion == 3:
    print('Djikstra\n')

  elif opcion == 4:
    print('Gracias por utilizar el programa\n')
    salir = True
