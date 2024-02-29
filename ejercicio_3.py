#!/usr/bin/python
#HACKERS_FIGHT_CLUB

from random import choice

calificacion_alumno = {}
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

def asigna_calificaciones():
    for b in becarios:
        calificacion_alumno[b] = choice(calificaciones)

def imprime_calificaciones():
    for alumno in calificacion_alumno:
        print('%s tiene %s\n' % (alumno,calificacion_alumno[alumno]))


def regresa_2tuplas():
    aprobados = []
    noAprobados = []
    for b in calificacion_alumno:
        if calificacion_alumno[b] > 8 or calificacion_alumno[b]==8:
            aprobados.append(b)
        elif calificacion_alumno[b] < 8:
            noAprobados.append(b)
    return ("aprobados",noAprobados),("noAProbados",noAprobados)

def promedio_calif():
    prom = 0.0
    for cal in calificacion_alumno[cal] :
        suma += cal
    prom = suma / len(calificacion_alumno)
    return prom

def conj_calf():
    ## entré tarde no alcancé a leer lo que pedian aqui xd 
    return ""