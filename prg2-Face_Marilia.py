##!/usr/bin/env python
# -*- coding: utf-8 -*-
# Marilia Ribeiro da Silva <marilia.ifc@gmail.com>
# prg2-Face_Marilia.py

'''
Escreva um programa que desenha algum tipo de face. 
'''
from graphics import *

def cria_janela(janela,x, y):
    janela = GraphWin('%s' %janela, x, y)
    return janela
    
def cria_retangulo(p1_x, p1_y, p2_x, p2_y, janela):
    retangulo = Rectangle(Point(p1_x, p1_y), Point(p2_x, p2_y))
    retangulo.setFill('#FFFF00')
    retangulo.setOutline('#FFFF00')
    retangulo.draw(janela)
    return retangulo
    
def cria_circulo(p1,p2,raio, janela):
    circulo = Circle(Point(p1,p2),raio)
    circulo.setFill('#FFFF00')
    circulo.setOutline('#B6B65B')
    circulo.draw(janela)
    return circulo

def cria_triangulo(p1_x, p1_y, p2_x, p2_y, p3_x, p3_y, janela):
    triangulo = Polygon(Point(p1_x, p1_y), Point(p2_x, p2_y), Point(p3_x, p3_y))
    triangulo.setFill('#FFFF00')
    triangulo.setOutline('#FFFF00')
    triangulo.draw(janela)
    return triangulo

def cria_linha(p1_x, p1_y, p2_x, p2_y, janela):
    linha = Line(Point(p1_x, p1_y), Point(p2_x, p2_y))
    linha.draw(janela)
    return linha
    
def fecha_janela(janela, x, y):
    janela.getMouse()
    janela.close()

def bart(janela, x, y):
    
    #orelhas
    orelhae = cria_circulo(190, 265, 15, janela)
    orelhad = cria_circulo(290, 265, 15, janela)
    
    orelhae2 = cria_linha(186, 262, 183, 268, janela)
    orelhae3 = cria_linha(183, 268, 188, 275, janela)
    orelhae3 = cria_linha(294, 261, 297, 267, janela)
    orelhae3 = cria_linha(297, 267, 293, 272, janela)

    # sombrancelhas
    sombrancelhae =  cria_circulo(198, 233, 10, janela)
    sombrancelhae.setOutline('#FFFF00')
    sombrancelhad = cria_circulo(282, 233, 10, janela)
    sombrancelhad.setOutline('#FFFF00')
    
    # rosto
    rosto = cria_retangulo(190, 165, 290, 330, janela)
    rosto2 = cria_retangulo(210, 300, 270, 340, janela)
    nariz = cria_circulo(240, 270, 12, janela)
    
    #olhos
    olhoe = cria_circulo(212, 250, 22, janela)
    olhoe.setFill('#FFFFFF')
    olhoe2 = cria_circulo(212, 250, 2, janela)
    olhoe2.setFill('#000000')
    olhod = cria_circulo(268, 250, 22, janela)
    olhod.setFill('#FFFFFF')
    olhod2 = cria_circulo(270, 250, 2, janela)
    olhod2.setFill('#000000')
    
    #boca
    boca1 = cria_linha(200, 315, 205, 310, janela)
    boca2 = cria_linha(205, 310, 280, 310, janela)
    boca3 = cria_linha(280, 310, 288, 319, janela)
    
    # cabelo
    for i in range(5):
        n = i * 20
        x1, x2, x3 = 190, 200, 210
        cabelo = cria_triangulo((x1 + n), 165, (x2 + n), 150, (x3 + n), 165, janela)
    
def main():
    janela = 'Rosto'
    x = 400
    y = 400
    
    janela = cria_janela(janela,x, y)
    bart(janela, x, y)
    fecha_janela(janela,x, y)
    

if __name__ == '__main__':
    main()

