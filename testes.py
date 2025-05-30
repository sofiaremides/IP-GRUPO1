import pygame as pg
from sys import exit
from classes_jogo import Tela_de_escolha

pg.init()
largura = 1280
altura = 720
tela = pg.display.set_mode((largura, altura))
menu = Tela_de_escolha(tela)
fps = pg.time.Clock()

while True:
    fps.tick(15)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            exit()
        menu.movimentacao_escolha(event)
    tela.fill((0, 0, 0))    
    menu.mostrar_texto()
    menu.triangulos_de_escolha()
    pg.display.update()
