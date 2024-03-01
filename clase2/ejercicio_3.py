#!/usr/bin/python
#HACKERS_FIGHT_CLUB

from random import choice
from poo1 import Alumno
import csv

calificacion_alumno = {} #diccionario que guarda las calif de cada alumno, la llave es el nombre
calificaciones = (0,1,2,3,4,5,6,7,8,9,10)
becarios = [
    'Abaustista Erick',
    'Anaya Pérez Ulises Josué',
    'Bautista Parra Jonathan',
    'Castro Rendón Diego',
    'Castro Sierra Etni Sarai',
    'Chavez Bolaños Gustavo',
    'Cornejo de la Mora Iñaki',
    'Cruz Hérnandez Víctor Emiliano',
    'Flores Cid Marco',
    'García Chavelas Jonás',
    'García Rosas Dicter Tadeo',
    'García Velasco Erick Iram',
    'Gónzalez Castro Diego Daniel',
    'Hernández Vela Daniel',
    'Isunza Álvarez Marcos Guillermo',
    'López Miranda Angel Mauricio',
    'López Prado Emiliano',
    'Monterrubio Acosta Demian Alejandro',
    'Navarro Santana Pablo César',
    'Ortíz Amaya Bruno Fernando',
    'Reyes López Eduardo Alfonso',
    'Reyes Trujillo Guadalupe',
    'Ríos Raúl', 
    'Trujillo Beltrán Zianya Nenetzi', 
    'Verano Peralta María Fernanda',
    'Vázquez Kuri Eduardo', 
    'Zurita León Dana Cecilia']


def leer_archivo(lista_completa,becarios):    
    with open(lista_completa,'r') as alumnos, open(becarios,'w',newline='') as lista_Becarios:
        CSV = csv.writer(lista_Becarios)
        for alumno in alumnos.readlines('\n'):
            nombre = alumno.strip()            
            calificacion = asigna_calificacion()
            CSV.writerow([nombre , calificacion])


def asigna_calificacion():
    return choice(calificaciones) #asigna calificacion a cada niño en el diccionario
        # {alumnoA: 9, alumnoB: 6, ....}

def asigna_calificaciones():
    for b in becarios:
        calificacion_alumno[b] = choice(calificaciones) #asigna calificacion a cada niño en el diccionario
        # {alumnoA: 9, alumnoB: 6, ....}

def imprime_calificaciones():
    for alumno in calificacion_alumno:
        print('%s tiene %s\n' % (alumno,calificacion_alumno[alumno]))


def regresa_2tuplas():
    aprobados = []
    noAprobados = []
    for b in becarios:
        if calificacion_alumno[b] > 8 or calificacion_alumno[b]==8:
            aprobados.append(b)
        else:
            noAprobados.append(b)
    return ("aprobados",aprobados),("noAProbados",noAprobados)

def promedio_calif():
    prom = 0.0
    suma = 0
    for cal in becarios:
        suma += calificacion_alumno[cal]
    prom = suma / len(calificacion_alumno)
    return prom

def conj_calf():
    ## entré tarde no alcancé a leer lo que pedian aqui );
    return ""

def lista_becarios():
    nombres = list(becarios.keys())
    listaBec = []
    for x in calificacion_alumno:
        alumno = Alumno(nombres[x],calificacion_alumno[x])
        listaBec.append(alumno)    
    return listaBec




"""
def main():    
    asigna_calificaciones()
    imprime_calificaciones()

    promedio = promedio_calif()
    print('El promedio de calificaciones es:', promedio)

    tuplas_aprobados_no_aprobados = regresa_2tuplas()
    print('Aprobados:', tuplas_aprobados_no_aprobados[0][1])
    print('No Aprobados:', tuplas_aprobados_no_aprobados[1][1])


if __name__ == "__main__":
    main()
"""