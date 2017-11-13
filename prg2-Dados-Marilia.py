#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Marilia Ribeiro da Silva <marilia.ifc@gmail.com>
# prg2-Dados_Marilia.py

'''
Escreva um programa que desenhe 5 dados na tela descrevendo uma sequência (1, 2, 3, 4, 5 ou 2, 3, 4, 5, 6).
'''

from graphics import *

def cria_janela(janela,x, y):
    janela = GraphWin('%s' %janela, x, y)
    return janela

def cria_circulo(p1,p2,janela):
    circulo = Circle(Point(p1,p2),10)
    circulo.setFill('#000000')
    circulo.setOutline('#000000')
    circulo.draw(janela)
    return circulo   

def cria_retangulo(p1_x, p1_y, p2_x, p2_y, janela):
    retangulo = Rectangle(Point(p1_x, p1_y), Point(p2_x, p2_y))
    retangulo.setFill('#FFFFFF')
    retangulo.setOutline('#FFFFFF')
    retangulo.draw(janela)
    return retangulo
    
def fecha_janela(janela, x, y):
    janela.getMouse()
    janela.close()
    
    
def pega_pontos(janela, x, y):
    for i in range(2):
         p = janela.getMouse()
         p.draw(janela)
         print('Você clicou em:', p.getX(), p.getY())
         
         
def cria_dados(janela, x, y):
    for i in range(5):
        n = i * 170        
        p1 = 30
        p2 = 170
        dado = cria_retangulo((p1 + n), 30,(p2+n),170, janela)
        if i == 0:
            num1 = cria_circulo(100, 110,janela)
        elif i == 1:
            num2 = cria_circulo(225, 70,janela)
            num2_2 = cria_circulo(305, 145, janela)
        elif i == 2:
            num1 = cria_circulo(445, 110, janela)
            num2 = cria_circulo(395, 70, janela)
            num3 = cria_circulo(490, 145, janela)
        elif i == 3:
            num1 = cria_circulo(570, 70, janela)
            num2 = cria_circulo(660, 70, janela)
            num3 = cria_circulo(570, 145, janela)
            num4 = cria_circulo(660, 145, janela)
        elif i == 4: 
            num1 = cria_circulo(780, 110, janela)
            num2 = cria_circulo(730, 70, janela)
            num3 = cria_circulo(830, 70, janela)
            num4 = cria_circulo(730, 145, janela)
            num5 = cria_circulo(833, 145, janela)


def main():
    janela = 'Dados'
    x = 900
    y = 200
    
    janela = cria_janela(janela,x, y)  
    cria_dados(janela, x, y)  
    #pega_pontos(janela, x, y)
    fecha_janela(janela,x, y)

if __name__ == '__main__':
    main()

