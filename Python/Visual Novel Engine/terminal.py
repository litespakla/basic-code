#!/usr/bin/env python
# -*- coding: utf-8 -*-

#Este código genera una aventura de texto a partir de las instrucciones encontradas en el archivo de texto "prueba.txt"

#Importa las librerías de Pygame que vamos a utilizar
import sys, pygame
from pygame.locals import *
import os
from pygame import mixer
import time

#Definimos las constantes que se van a utilizar a lo largo del código
l=[]
historia=[]
parte=[]
final=[]
personaje=[]
ancho=0
largo=0
numero_de_linea=0
caja=0
musica=""
imagen=""
titulo=""
persona=""

#Abrimos el archivo de texto
juego = open('prueba.txt', 'r')

#Guarda cada línea del archivo en una posición del vector l, excepto las líneas en blanco y las que empiezan con el símbolo "#" (comentarios)
for line in juego:
    if line[0]!="#" and line[0]!="\n":
       l.append(line)

#Cerramos el archivo de texto
juego.close()

#Carga los parámetros para la interfaz de Pygame y la imágen, música y sprites de la pantalla de inicio del juego.
while l[numero_de_linea][0]!="@":
    palabra=l[numero_de_linea].split()
    if palabra[0]=="MUSICA:":
        musica=palabra[1]

    numero_de_linea+=1

#Mueve el contador a la siguiente línea
numero_de_linea+=1

#Carga los nombres de los personajes del juego
while l[numero_de_linea][0]!="-":
    palabra=l[numero_de_linea].split()
    for i in range(2, len(palabra)):
        persona+=palabra[i] + " "
    personaje.append(persona)
    persona=""
    numero_de_linea+=1

#Mueve el contador a la siguiente línea
numero_de_linea+=1

#Crea la matriz "historia" y la matriz "finales". La primera posición corresponde al bloque de historia y la segunda al número de línea
while l[numero_de_linea]!="<>\n":
    if l[numero_de_linea][0]=="/":
        numero_de_linea+=1
        while l[numero_de_linea][0]!="/":
            parte.append(l[numero_de_linea])
            numero_de_linea+=1
        historia.append(parte)
        parte=[]
    elif l[numero_de_linea][0]=="&":
       numero_de_linea+=1
       while l[numero_de_linea][0]!=".":
           parte.append(l[numero_de_linea])
           numero_de_linea+=1
       final.append(parte)
       parte=[]
    numero_de_linea+=1

# Limpia la variable l para liberar memoria
l=[]

#
def opciones(lista, a):
    i=a
    opcion=""
    while lista[i][0]!="*":
        palabra=lista[i].split()
        for j in range(0, len(palabra)-2):
            opcion+=palabra[j] + " "
        print opcion
        opcion=""
        i+=1
    print "\nEscoge alguna de las opciones entre ", 1, "y", lista[i-1][0]
    while True:
        try:
            x = int(input())
            while not 1<=x<=int(lista[i-1][0]):
                print "No entiendo lo que quieres hacer :("
                x=input()
            break
        except (NameError, SyntaxError):
            print "No entiendo lo que quieres hacer :("
    for j in range(a,i):
        if int(lista[j][0])==x:
            palabra=lista[j].split()
            marcador=palabra[len(palabra)-2]
            numero=palabra[len(palabra)-1]
    os.system("clear")
    if marcador=="/":
        trama(historia[int(numero)], marcador)
    elif marcador=="&":
        trama(final[int(numero)],marcador)

def trama(lista, marcador):
    i=0
    while i in range(0,len(lista)):
        palabra=lista[i].split()
        if palabra[0]=="+musica:":
            try:
                mixer.music.load(palabra[1])
                mixer.music.play(-1, int(palabra[2]))
            except IndexError:
                mixer.music.load(palabra[1])
                mixer.music.play(-1)
            i+=1
            time.sleep(0.8)
        elif palabra[0]=="+imagen:":
            i+=1
        elif palabra[0]=="+p.":
            i+=1
        elif palabra[0]=="*":
            a=i+1
            i=len(lista)
            print "\n",
        else:
            print lista[i],
            i+=1
            time.sleep(1.7)
    if marcador=="/":
        opciones(lista, a)
    elif marcador=="&":
        x=raw_input("\nGAME OVER\nPlay again? (y/n)\n")
        if x=="y":
            os.system("clear")
            print "NUEVO JUEGO\n"
            trama(historia[0], "/")
        elif x=="n":
            return marcador
    return 0

os.system("clear")
mixer.init()
trama(historia[0], "/")
