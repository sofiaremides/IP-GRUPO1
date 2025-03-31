import pygame as pg
from random import randint
class Inimigo:
    def __init__(self,tela,velocidade):
        self.vivo = True
        self.posicao_x = randint(0,1280)
        self.posicao_y = randint(0,720)
        self.velocidade = velocidade
        self.tela = tela
        self.rect = pg.Rect(self.posicao_x,self.posicao_y,32,32)

    def movimentacao(self,alvo_x,alvo_y):
        if alvo_x > self.posicao_x:
            self.posicao_x += self.velocidade
        if alvo_x < self.posicao_x:
            self.posicao_x += -self.velocidade
        if alvo_y > self.posicao_y:
            self.posicao_y += self.velocidade
        if alvo_y < self.posicao_y:
            self.posicao_y += -self.velocidade

    def morrer(self):
        self.vivo = False

    def existir(self):
        pg.draw.rect(self.tela,('Purple'),(self.posicao_x,self.posicao_y,32,32))
        #atualizar a posição do retângulo para calcular a colisão
        self.rect = pg.Rect(self.posicao_x,self.posicao_y,32,32)