#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Marilia Ribeiro da Silva <marilia.ifc@gmail.com>
# prg2-Bandeira_Marilia.py

'''
Escreva um programa que desenhe a bandeira de um país a sua escolha.
'''

from graphics import *

def cria_janela(janela,x, y):
    janela = GraphWin('%s' %janela, x, y)
    return janela
    
def cria_retangulo(p1_x, p1_y, p2_x, p2_y, janela):
    retangulo = Rectangle(Point(p1_x, p1_y), Point(p2_x, p2_y))
    retangulo.setFill('#008000')
    retangulo.setOutline('#008000')
    retangulo.draw(janela)
    return retangulo
    
def cria_circulo(p1,p2,raio, janela):
    circulo = Circle(Point(p1,p2),raio)
    circulo.setFill('#4524AA')
    circulo.setOutline('#4524AA')
    circulo.draw(janela)
    return circulo
    
def cria_triangulo(p1_x, p1_y, p2_x, p2_y, p3_x, p3_y, p4_x, p4_y, janela):
    triangulo = Polygon(Point(p1_x, p1_y), Point(p2_x, p2_y), Point(p3_x, p3_y), Point(p4_x, p4_y))
    triangulo.setFill('#FFFF00')
    triangulo.setOutline('#FFFF00')
    triangulo.draw(janela)
    return triangulo

def fecha_janela(janela, x, y):
    janela.getMouse()
    janela.close()
            
def bandeira(janela, x, y ):         
    bandeira1 = cria_retangulo(0,0, 500, 300, janela)
    bandeira2 = cria_triangulo(250, 20, 20, 150, 250, 280, 480, 150, janela)
    bandeira3 = cria_circulo(250, 150, 100, janela)
    faixa = cria_retangulo(150, 135, 350, 165, janela)
    faixa.setFill('#FFFFFF')
    texto = Text(Point(250, 150), 'Ordem e Progresso')
    texto.draw(janela)
    
    
def main():
    janela = 'Bandeira'
    x = 500
    y = 300
    
    janela = cria_janela(janela,x, y)
    bandeira(janela, x, y)
    fecha_janela(janela,x, y)
   
if __name__ == '__main__':
    main()

