#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Marilia Ribeiro da Silva <marilia.ifc@gmail.com>
# prg2-Natal_Marilia.py

'''
Escreva um programa que desenhe uma cena de inverno com uma árvore de Natal e um boneco de neve. 
'''
from graphics import *

def cria_janela(janela,x, y):
    janela = GraphWin('%s' %janela, x, y)
    return janela

def cria_triangulo(p1, p2, p3):
    triangulo = Polygon(p1,p2,p3)
    triangulo.setFill('#1C5A1C')
    triangulo.setOutline('#1C5A1C')
    time.sleep(0.3)
    return triangulo
    
def cria_circulo(p1,p2,raio):
    circulo = Circle(Point(p1,p2),raio)
    circulo.setFill('#fdf5e6')
    circulo.setOutline('#fdf5e6')
    time.sleep(0.3)
    return circulo   

def cria_linha(p1_x, p1_y, p2_x, p2_y, janela):
    linha = Line(Point(p1_x, p1_y), Point(p2_x, p2_y))
    linha.draw(janela)
    return linha
    
def cria_retangulo(p1_x, p1_y, p2_x, p2_y, janela):
    retangulo = Rectangle(Point(p1_x, p1_y), Point(p2_x, p2_y))
    retangulo.draw(janela)
    return retangulo

def cria_arvore(janela, x, y):

    # copa_arvore
    arvore = cria_triangulo(Point(250, 50), Point(200, 150), Point(300, 150))
    arvore.draw(janela)
    
    # meio_arvore
    arvore = cria_triangulo(Point(250, 100), Point(150, 250), Point(350, 250))
    arvore.draw(janela)
    
    # fim_arvore
    arvore = cria_triangulo(Point(250, 150), Point(100, 350), Point(400, 350))
    arvore.draw(janela)
    
    #tronco
    tronco = cria_retangulo(220, 350,280,480, janela)
    tronco.setFill('#814F1C')
    tronco.setOutline('#814F1C')

def boneco_neve(janela, x, y):
    #base - corpo
    corpo = cria_circulo(550, 400, 80)
    corpo.draw(janela)
    
    # gorro    
    gorro = cria_circulo(550, 340, 40)
    gorro.setFill('#F11A1A')
    gorro.setOutline('#F11A1A')
    gorro.draw(janela)
    
    gorro_laco = cria_retangulo(570,345,590,400, janela)
    gorro_laco.setFill('#F11A1A')
    gorro_laco.setOutline('#F11A1A')
    
    # cabeça
    cabeca = cria_circulo(550, 300, 50)
    cabeca.draw(janela)
    
    # olhos
    olhod = cria_circulo(525, 290, 5)
    olhod.setFill('#000000')
    olhod.draw(janela)
    
    olhod = cria_circulo(570, 290, 5)
    olhod.setFill('#000000')
    olhod.draw(janela)
    
    # nariz
    nariz = cria_circulo(548, 310, 5)
    nariz.setFill('#ED7D11')
    nariz.setOutline('#ED7D11')
    nariz.draw(janela)
    
    # boca    
    boca1 = cria_linha(525, 325, 540, 340, janela)
    boca2 = cria_linha(540, 340, 560, 340, janela)
    boca3 = cria_linha(560, 340, 575, 325, janela)
    
    # braços
    bracoe = cria_linha(490, 380, 455, 330, janela)
    bracod = cria_linha(615, 380, 645, 330, janela)
    
    #mão
    dedo1 = cria_linha(455, 330, 464, 310, janela)
    dedo2 = cria_linha(455, 330, 442, 315, janela)
    dedo3 = cria_linha(455, 330, 437, 338, janela)
    dedo4 = cria_linha(645, 330, 640, 315, janela)
    dedo5 = cria_linha(645, 330, 664, 310, janela)
    dedo6 = cria_linha(645, 330, 674, 329, janela)
    
    # chapéu
    chapeu = cria_retangulo(500,250,600,270, janela)
    chapeu.setFill('#FFFFFF')
    chapeu.setOutline('#FFFFFF')
    
    chapeu2 = cria_triangulo(Point(509, 250), Point(594, 223), Point(645, 264))
    chapeu2.setFill('#F11A1A')
    chapeu2.setOutline('#F11A1A')
    chapeu2.draw(janela)
    
    pompom = cria_circulo(651, 268, 10)
    pompom.setFill('#FFFFFF')
    pompom.setOutline('#FFFFFF')
    pompom.draw(janela)
    
def fecha_janela(janela, x, y):
    janela.getMouse()
    janela.close()
    
def main():
    print('Este programa cria uma cena de natal.')
    janela = 'Natal'
    x = 800
    y = 500
    
    janela = cria_janela(janela,x, y)
    cria_arvore(janela, x, y)
    boneco_neve(janela, x, y)    
    fecha_janela(janela,x, y)    

if __name__ == '__main__':
    main()

 

