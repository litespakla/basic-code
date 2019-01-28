#!/usr/bin/env python
# -*- coding: utf-8 -*-

from itertools import permutations

def prueba(solucion, dic):
    x=0
    #x=1
    for num in solucion:
        x+=num
        #x*=num
    if x==2*solucion[len(solucion)-1]:
        print solucion, dic

alpha=raw_input('Enter alphametic\n')

#Creamos el diccionario
diccionario={}
words=[]
palabra=''
solucion=[]

for char in alpha:

    #Si la letra no está en el diccionario la agrega
    if diccionario.get(char)==None and char!='=' and char!='+':
        diccionario[char]=-1

    if char!='=' and char !='+':
        palabra+=char
    else:
        words.append(palabra)
        palabra=''

a=list(permutations(range(10), len(diccionario.keys())))
i=0
numero=0
resultado=0

for lista in a:
    k=1
    for key in diccionario:
        diccionario[key]=lista[i]
        i+=1
    i=0
    for word in words:
        j=len(word)-1
        for letra in word:
            numero+=diccionario[letra]*pow(10, j)
            j-=1
        solucion.append(numero)
        numero=0
    j=len(palabra)-1
    for letra in palabra:
        resultado+=diccionario[letra]*pow(10, j)
        j-=1
    solucion.append(resultado)
    for word in words:
        if diccionario[word[0]]==0:
            k-=1
    if diccionario[palabra[0]]==0:
        k-=1
    if k==1:
        prueba(solucion, diccionario)
    solucion=[]
    resultado=0
