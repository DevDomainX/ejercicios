#!/usr/bin/env python3
# Creador Hans saldias - script de ejercicios V1
from  random import randint
import os
from time import sleep
import sys

def menu():
    print("""\033[33m
    Bienvenido al progarma de entrenamiento elija una opcion del menu

    Created by: Hans saldias

    Programa creado para camilo Vamos!!!

    1 - Ejercicios a piso 

    2 - cuantas ases en un minuto

    0 - salir del programa
    """)

def piso():
    ejercicios = ['Lagartijas', 'Diamantes', 'polichilenas', 'abdominales']
    for i in ejercicios:
        num = randint(1, 70)
        print(f"\n\nEl reto de hoy es \033[32m{num}\033[0m \033[32m{i}\033[0m\n\n")
        input("\033[32mSI ESTAS LISTO APRETA ENTER PARA PASAR AL OTRO EJERCICIO?\033[0m ")
        os.system("clear")
    print("\033[42mFin de los ejercicios de piso\033[0m]")
    q = input("Deseas volver al menu? (si/no): ").strip().lower()
    if q == "si":
        menu()
    else:
        sys.exit()

def resistencia():
    print("\n\n\033[35mAl preionar enter te dictara un ejercicio con tiempo de un minuto tienes que aser los mas que puedas en ese tiempo\033[0m\n\n")
    listo = input("\033[34mEstas listo para empesar? prsiona enter\033[0m")
    cont = 60
    for i in range(60):
        print("\t\tVAMOS CAMILO TU PUEDES!!!\n\n")
        print("El ejercicio es {} TIEMPO \033[32m{}\033[0m".format("Lagartijas",cont-i))
        sleep(0.5)
        os.system("cls")
    
    print("\n\n\033[35mAl preionar enter te dictara un ejercicio con tiempo de un minuto tienes que aser los mas que puedas en ese tiempo\033[0m\n\n")
    listo = input("\033[34mEstas listo para empesar? prsiona enter\033[0m")
    q = input("Exelente ejercicio terminado presiona enter para comenzar con el otro").strip().lower()
    for i in range(60):
        print("\t\tVAMOS CAMILO TU PUEDES!!!\n\n")
        print("El ejercicio es {} TIEMPO {}".format("Abdominales",cont-i))
        sleep(0.5)
        os.system("cls")

    print("\n\n\033[35mAl preionar enter te dictara un ejercicio con tiempo de un minuto tienes que aser los mas que puedas en ese tiempo\033[0m\n\n")
    listo = input("\033[34mEstas listo para empesar? prsiona enter\033[0m")
    q = input("Exelente ejercicio terminado presiona enter para comenzar con el otro").strip().lower()
    cont = 120
    for i in range(120):
        print("\t\tVAMOS CAMILO TU PUEDES!!!\n\n")
        print("El ejercicio es {} TIEMPO {}".format("polichilenas",cont-i))
        sleep(0.5)
        os.system("cls")

    print("\n\n\033[35mAl preionar enter te dictara un ejercicio con tiempo de un minuto tienes que aser los mas que puedas en ese tiempo\033[0m\n\n")
    listo = input("\033[34mEstas listo para empesar? prsiona enter\033[0m")
    q = input("Exelente ejercicio terminado presiona enter para comenzar con el otro").strip().lower()
    cont = 60
    for i in range(60):
        print("\t\tVAMOS CAMILO TU PUEDES!!!\n\n")
        print("El ejercicio es {} TIEMPO {}".format("Diamantes",cont-i))
        sleep(0.5)
        os.system("cls")

os.system("cls")
while True:
    try:
        menu()
        op = int(input("Ingrese la opcion: "))
        if op == 1:
            piso()
        elif op == 2:
            resistencia()
        elif op == 0:
            print("Hasta pronto\n\n")
            break


    except ValueError:
        print("la opcion ingresada no es valida, intente nuevamente ")