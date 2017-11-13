#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Marilia Ribeiro da Silva <marilia.ifc@gmail.com>
# prg2-Alvo_Marilia.py

'''
Um alvo de tiro com arco é composto por um círculo central amarelo cercado por anéis concêntricos em vermelho, azul, 
preto e branco. Cada anel tem a mesma "largura", que é o mesma que o raio do círculo amarelo. 
Escreva um programa que desenhe esse alvo. Dica: objetos desenhados mais tarde irá aparecer em cima dos objetos desenhados 
antes. 
'''

from graphics import *

def cria_janela(janela,tamanho):
    janela = GraphWin('%s' %janela,tamanho, tamanho)
    return janela

def cria_circulo(raio):
    circulo = Circle(Point(250, 250),raio)
    time.sleep(0.3)
    return circulo

def cria_alvo(janela, tamanho):
    
    # anél branco
    branco = '#FFFFFF'
    raio = 250
    circulo1 = cria_circulo(raio)
    circulo1.setFill(branco)
    circulo1.setOutline(branco)
    circulo1.draw(janela)
    
     # anél preto
    preto = '#000000'
    raio = 200
    circulo2 = cria_circulo(raio)
    circulo2.setFill(preto)
    circulo2.setOutline(preto)
    circulo2.draw(janela)
    
    # anél azul
    azul = '#0000FF'
    raio = 150
    circulo3 = cria_circulo(raio)
    circulo3.setFill(azul)
    circulo3.setOutline(azul)
    circulo3.draw(janela)
    
    # anél vermelho
    vermelho = '#FF0000'
    raio = 100
    circulo4 = cria_circulo(raio)
    circulo4.setFill(vermelho)
    circulo4.setOutline(vermelho)
    circulo4.draw(janela)
    
    # circulo amarelo
    amarelo = '#FFFF00'
    raio = 50
    circulo5 = cria_circulo(raio)
    circulo5.setFill(amarelo)
    circulo5.setOutline(amarelo)
    circulo5.draw(janela)

def fecha_janela(janela,tamanho):
    janela.getMouse()
    janela.close()

def main():
    print('Este programa cria uma animação de um alvo de Arco e Flexa. \n')
    janela = 'Alvo'
    tamanho = 500
    
    janela = cria_janela(janela, tamanho)
    cria_alvo(janela, tamanho)
    fecha_janela(janela,tamanho)


if __name__ == '__main__':
    main()




