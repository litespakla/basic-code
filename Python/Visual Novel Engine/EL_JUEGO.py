#!/usr/bin/env python
# -*- coding: utf-8 -*-

#Este código genera una aventura de texto a partir de las instrucciones encontradas en el archivo de texto "texto.txt"

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
guardar=[]
ancho=0
largo=0
numero_de_linea=0
caja=0
indice=0
musica=""
imagen=""
titulo=""
persona=""
ventanaTexto=""
picture=""
screen=""
colorT=""
colorN=""
colorB=""
colorS=""
colorM=""
letraM=0
letraT=0
letra0=0
letraN=0
fuente="NONE"

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
    if palabra[0]=="TITULO_DEL_JUEGO:":
        for i in range(1, len(palabra)):
            titulo+=palabra[i] + " "
    elif palabra[0]=="ANCHO:":
        ancho=int(palabra[1])
    elif palabra[0]=="LARGO:":
        largo=int(palabra[1])
    elif palabra[0]=="CAJA:":
        caja=int(palabra[1])
    elif palabra[0]=="MUSICA:":
        musica=palabra[1]
    elif palabra[0]=="IMAGENES:":
        imagen=palabra[1]
    elif palabra[0]=="VENTANA_DE_TEXTO:":
        ventanaTexto=palabra[1]
    elif palabra[0]=="FUENTE:":
        fuente=palabra[1]
    elif palabra[0]=="COLOR_TEXTO:":
        colorT=(int(palabra[1]), int(palabra[2]), int(palabra[3]))
    elif palabra[0]=="COLOR_NOMBRE:":
        colorN=(int(palabra[1]), int(palabra[2]), int(palabra[3]))
    elif palabra[0]=="COLOR_BOTONES:":
        colorB=(int(palabra[1]), int(palabra[2]), int(palabra[3]))
    elif palabra[0]=="COLOR_MENU:":
        colorM=(int(palabra[1]), int(palabra[2]), int(palabra[3]))
    elif palabra[0]=="COLOR_SELECCION:":
        colorS=(int(palabra[1]), int(palabra[2]), int(palabra[3]))
    elif palabra[0]=="TAMANO_LETRA_MENU:":
        letraM=int(palabra[1])
    elif palabra[0]=="TAMANO_LETRA_TEXTO:":
        letraT=int(palabra[1])
    elif palabra[0]=="TAMANO_LETRA_NOMBRE:":
        letraN=int(palabra[1])
    elif palabra[0]=="TAMANO_LETRA_OPCIONES:":
        letraO=int(palabra[1])
    numero_de_linea+=1

#Mueve el contador a la siguiente línea
numero_de_linea+=1

#Carga los nombres de los personajes del juego
while l[numero_de_linea][0]!="-":
    palabra=l[numero_de_linea].split()
    for i in range(2, len(palabra)):
        persona+=palabra[i].decode('utf-8') + " "
    personaje.append(persona)
    persona=""
    numero_de_linea+=1

#Mueve el contador a la siguiente línea
numero_de_linea+=1

#
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

#Carga las imágenes de fondo
def load_image(filename):
        image = pygame.image.load(filename)
        image = image.convert()
        size=[ancho, largo]
        image= pygame.transform.scale(image, size)
        return image

#Cambia la imagen de fondo
def cambiarImagen(nuevaImagen):
    background_image = load_image(nuevaImagen)
    ventana=pygame.image.load(ventanaTexto)
    ventana= pygame.transform.scale(ventana, [8*ancho/10, caja])
    screen.blit(background_image, (0, 0))
    screen.blit(ventana, (0.1*ancho, largo-caja-(0.02*largo)))
    pygame.display.flip()

#
def personajes(numero):
    perso=pygame.image.load(pers)
    font = pygame.font.SysFont(fuente, letraN)
    texto = font.render(personaje[numero], 0, colorN)
    ventana=pygame.image.load(ventanaTexto)
    ventana= pygame.transform.scale(ventana, [8*ancho/10, caja])
    perso= pygame.transform.scale(perso, [16*ancho/100, 82*caja/100])
    screen.blit(ventana, (0.1*ancho, largo-caja-(0.02*largo)))
    screen.blit(perso, (0.113*ancho, largo-caja-(0.006*largo)))
    screen.blit(texto, (0.28*ancho, largo-caja-(0.00007*caja)))
    pygame.display.flip()

#
def fondo():
    background_image = load_image(picture)
    screen.blit(background_image, (0, 0))
    pygame.display.flip()

#
def opciones(lista, a):
    i=a
    opcion=""
    botones=[]
    salir=False
    listaM={}
    fondo()
    while lista[i][0]!="*":
        palabra=lista[i].split()
        for j in range(1, len(palabra)-2):
            opcion+= palabra[j].decode('utf-8') + " "
        marcador=palabra[len(palabra)-2]
        numero=int(palabra[len(palabra)-1])
        b=(opcion, trama)
        botones.append(b)
        listaM[opcion]=(numero, marcador)
        opcion=""
        i+=1
    menu = choices(botones)
    while not salir:

        for e in pygame.event.get():
            if e.type == QUIT:
                salir = True

        menu.actualizar(listaM)
        menu.imprimir(screen)

        pygame.display.flip()
        pygame.time.delay(10)

#no doc
def trama(lista, marcador):
    i=0
    global picture
    global pers
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
            picture=palabra[1]
            cambiarImagen(picture)
            i+=1
        elif palabra[0]=="+p.":
            if palabra[1]!="x":
                pers=palabra[2]
                c=int(palabra[1])-1
                personajes(c)
            else:
                cambiarImagen(picture)
            i+=1
        elif palabra[0]=="*":
            a=i+1
            i=len(lista)
        else:
            font = pygame.font.SysFont(fuente, letraT)
            words = [word.split(' ') for word in lista[i].splitlines()]  # 2D array where each row is a list of words.
            space = font.size(' ')[0]  # The width of a space.
            max_width, max_height = (87*ancho/100, caja)
            pos = (0.28*ancho, largo-caja-(0.02*largo)+0.066*largo)
            x, y = pos
            for line in words:
                for word in line:
                    word = word.decode('utf-8')
                    word_surface = font.render(word, 0, colorT)
                    word_width, word_height = word_surface.get_size()
                    if x + word_width >= max_width:
                        x = pos[0]  # Reset the x.
                        y += word_height  # Start on new row.
                    screen.blit(word_surface, (x, y))
                    x += word_width + space
                x = pos[0]  # Reset the x.
                y += word_height
            pygame.display.flip()
            time.sleep(0.2)

            for event in pygame.event.get():
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_SPACE:
                        i+=1
                        try:
                            personajes(c)
                        except UnboundLocalError:
                            cambiarImagen(picture)
                    elif event.key==pygame.K_ESCAPE:
                        sys.exit(0)
                    elif event.key==pygame.K_BACKSPACE:
                        main()
                    elif event.key==pygame.K_g:
                        f = open ("saves.txt", "w")
                        f.write("%s %s" %(marcador, indice))
                        f.close()
                        print "Juego guardado"

    if marcador=="/":
        opciones(lista, a)
    if marcador=="&":
        main()
    return

class Menu:
    "Representa un menú con opciones para un juego"

    def __init__(self, options):
        self.options = options
        self.font = pygame.font.SysFont(fuente, letraM)
        self.seleccionado = 0
        self.total = len(self.options)
        self.mantiene_pulsado = False

    def actualizar(self):
        """Altera el valor de 'self.seleccionado' con los direccionales."""

        k = pygame.key.get_pressed()

        if not self.mantiene_pulsado:
            if k[K_UP]:
                self.seleccionado -= 1
            elif k[K_DOWN]:
                self.seleccionado += 1
            elif k[K_RETURN]:

                # Invoca a la función asociada a la opción.
                title, funcion = self.options[self.seleccionado]
                funcion()

        # procura que el cursor esté entre las opciones permitidas
        if self.seleccionado < 0:
            self.seleccionado = 0
        elif self.seleccionado > self.total - 1:
            self.seleccionado = self.total - 1

        # indica si el usuario mantiene pulsada alguna tecla.
        self.mantiene_pulsado = k[K_UP] or k[K_DOWN] or k[K_RETURN]


    def imprimir(self, screen):
        """Imprime sobre 'screen' el texto de cada opción del menú."""

        total = self.total
        indice = 0
        altura_de_opcion = largo/3
        x = 0.25*ancho
        y = 0.15*largo

        for (title, funcion) in self.options:
            if indice == self.seleccionado:
                color = colorS
            else:
                color = colorM

            imagen = self.font.render(title, 1, color)
            posicion = (x, y + altura_de_opcion * indice)
            indice += 1
            screen.blit(imagen, posicion)

class choices:
    "Representa un menú con opciones para un juego"

    def __init__(self, options):
        self.options = options
        self.font = pygame.font.SysFont(fuente, letraO)
        self.seleccionado = 0
        self.total = len(self.options)
        self.mantiene_pulsado = False

    def actualizar(self, hoja):
        """Altera el valor de 'self.seleccionado' con los direccionales."""

        k = pygame.key.get_pressed()

        if not self.mantiene_pulsado:
            if k[K_UP]:
                self.seleccionado -= 1
            elif k[K_DOWN]:
                self.seleccionado += 1
            elif k[K_RETURN]:

                # Invoca a la función asociada a la opción.
                title, funcion = self.options[self.seleccionado]
                destino=hoja[title]
                cambiarImagen(picture)
                global indice
                indice=destino[0]
                if destino[1]=="/":
                    funcion(historia[destino[0]], destino[1])
                elif destino[1]=="&":
                    funcion(final[destino[0]], destino[1])

        # procura que el cursor esté entre las opciones permitidas
        if self.seleccionado < 0:
            self.seleccionado = 0
        elif self.seleccionado > self.total - 1:
            self.seleccionado = self.total - 1

        # indica si el usuario mantiene pulsada alguna tecla.
        self.mantiene_pulsado = k[K_UP] or k[K_DOWN] or k[K_RETURN]


    def imprimir(self, screen):
        """Imprime sobre 'screen' el texto de cada opción del menú."""

        total = self.total
        indice = 0
        altura_de_opcion = largo*0.7/(len(self.options))
        x = 0.08*ancho
        y = 0.15*largo

        for (title, funcion) in self.options:
            title=u''.join(title)
            if indice == self.seleccionado:
                color = colorS
            else:
                color = colorB

            imagen = self.font.render(title, 1, color)
            posicion = (x, y + altura_de_opcion * indice)
            indice += 1
            screen.blit(imagen, posicion)

def comenzar_nuevo_juego():
    os.system("clear")
    global indice
    indice=0
    trama(historia[0], "/")

def continuar():
    os.system("clear")

    #Si existe un juego guardado
    try:
        f = open ("saves.txt", "r")
        for line in f:
            guardar=line.split()
        f.close()
    except:
        pass

    time.sleep(0.1)
    try:
        global indice
        indice=int(guardar[1])
        print guardar[0]
        if guardar[0]=="/":
            trama(historia[indice], guardar[0])
        elif guardar[0]=="&":
            trama(final[indice], guardar[0])
    except Exception as e:
        print "No hay juego guardado"
        main()

def salir_del_programa():
    print "Gracias por utilizar este programa."
    sys.exit(0)


def main():
    salir = False
    options = [
        ("Jugar", comenzar_nuevo_juego),
        ("Continuar", continuar),
        ("Salir", salir_del_programa),
        ]

    pygame.font.init()
    global screen
    screen = pygame.display.set_mode((ancho, largo))
    pygame.display.set_caption(titulo)
    background_image = load_image(imagen)
    menu = Menu(options)
    mixer.init()
    mixer.music.load(musica)
    mixer.music.play(-1)

    while not salir:

        for e in pygame.event.get():
            if e.type == QUIT:
                salir = True

        screen.blit(background_image, (0, 0))
        menu.actualizar()
        menu.imprimir(screen)

        pygame.display.flip()
        pygame.time.delay(10)

if __name__ == '__main__':
    main()
