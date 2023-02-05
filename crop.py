#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
import sys
import re
import os
from PIL import Image
from pathlib import Path

def crop(ImageToCrop):
    #
    # on ouvre l'image. On se fout si c'est pas une image ou si le format n'est pas supporté
    #
    im = Image.open(ImageToCrop)
    px = im.load()
    #
    # On met la couleur blanche en RVB, la tolérance pour chaque couleur, la largeur*hauteur d'une page A4 en pixel
    #
    RVB = (250,250,250)
    coefMax = 1.10
    coefMin = 0.90
    maxR = RVB[0] * coefMax
    minR = RVB[0] * coefMin
    maxV = RVB[1] * coefMax
    minV = RVB[1] * coefMin
    maxB = RVB[2] * coefMax
    minB = RVB[2] * coefMin
    largeur=2481
    hauteur=3501
    #
    # Le rayon sert ici à ne pas démarrer au bord et à définir le nombre de pixels contigus qui s'approchent (maxR...) de la couleur de référence (RVB)
    #
    rayon=200
    #
    # On va chercher l'adresse x de la première série (nb rayon) qui correspond à RVB
    #
    occur = 0
    y=rayon
    for x in range(rayon+1,largeur-rayon-1):
        RVB = px[x,y]
        if  (minR < RVB[0] < maxR) and (minV < RVB[1] < maxV) and (minB < RVB[2] < maxB):
            occur += 1
        else:
            occur = 0
        if occur == rayon:
            break
    X = x - rayon
    #
    # On va chercher l'adresse y de la première série (nb rayon) qui correspond à RVB
    #

    x=rayon
    occur = 0
    for y in range(rayon+1,hauteur-rayon-1):
        RVB = px[x,y]
        if  (minR < RVB[0] < maxR) and (minV < RVB[1] < maxV) and (minB < RVB[2] < maxB):
            occur += 1
        else:
            occur = 0
        if occur == rayon:
            break
    Y = y - rayon
    #
    print(X,Y)
    #
    # et enfin on découpe et on sauvegarde avec extension _cropped.jpg'
    #
    cropped = im.crop((0,0,X,Y))
    FileWithoutExtension = os.path.splitext(ImageToCrop)[0]
    FinalPicture = FileWithoutExtension + '_cropped.jpg'
    cropped.save(FinalPicture,'JPEG')
    return()

if __name__ == '__main__':
    #
    # si pas d'argument --> exit
    #
    try:
        FileToCrop = sys.argv[1]
    except:
        exit()
    crop(FileToCrop)
    exit()