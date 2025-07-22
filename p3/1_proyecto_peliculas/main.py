import mysql.connector
from mysql.connector import Error
#proyecto 1 crear un proyecto que permita  gestionar (administrar peliculas) colocar un menu de opciones para agregar: borrar, modificar, consultar, buscar

#notas: 
# 1 utilizar funciones y mandar llamar desde otro archivo
#2 utilizar una lista para almacenar los nombres
#3 utilizar e implementar una base de datos relacionar en SQL
import os
os.system("cls")
import peliculas



#peliculas=[
 # ["gran turismo"],
  #["rapidos y furiosos 5"],
  #["ted 2"],
  #["mad max"],
  #["conjuro 3"],
  #["lluvia de hambuerguesas"],
  #["star wars"],
  #]

opcion=True
while opcion:
  peliculas.borrarPantalla()
  print("\n\t..::: CINEPOLIS CLON :::... \n..::: Sistema de Gestión de Peliculas :::...\n 1.- crear \n 2.- borrar \n 3.- mostrar \n 4.- Buscar \n 5.- Modificar \n 6.- SALIR ")
  opcion=input("\t Elige una opción: ").upper()

  match opcion:
        case "1":
            peliculas.crearpeliculas()
            peliculas.esperarTecla()
        case "2":
            peliculas.borrarpeliculas()
            peliculas.esperarTecla()
        case "3":
            peliculas.mostrarpeliculas()
            peliculas.esperarTecla()
        case "4":
            peliculas.buscarpeliculas() 
            peliculas.esperarTecla()
        case "5": 
            peliculas.modificarpeliculas()
            peliculas.esperarTecla()
        case "6":
            opcion=False    
            print(f"\n\"Terminaste la ejecucion del SW")
        case _: 
            input(f"\n\"Opción invalida vuelva a intentarlo ... por favor")