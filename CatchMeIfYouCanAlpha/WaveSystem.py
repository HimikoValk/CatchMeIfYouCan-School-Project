from enum import EnumMeta
from html import entities
from random import randrange


import pygame
from Enemy import EntityEnemy
from Player import Player
class Wave(): 
    wave_counter = 1
    entities = []

    def __init__(self,player):
        self.player = player
        self.add_enemy()
    

    def cal_wave(self): 
        return self.wave_counter * self.player.hearts

    def cal_timer(self): 
        return self.cal_wave() * 10


    def wave_system(self, screen, font): 
        color = (50, 168, 82)
        timer = 0
        screen.blit(font.render("Time:"+ str(timer), True, color), (600, 0))
        if(timer != 0): 
            timer -= 1
        #self.remove_enemies()
        #self.wave_counter += 1
        #pygame.time.delay(2000)
        self.add_enemy()
        #timer = self.cal_timer()
        self.create_enemies_on_screen(screen)
    

    def create_enemies_on_screen(self, screen, attack_player): 
        for enemies in self.entities: 
            if(attack_player == True): 
                enemies[1].draw(screen)
                enemies[1].draw_rect(screen)
                enemies[1].move(True, 0.15, player=self.player)
            else:
                self.remove_enemies()
    
    def remove_enemies(self): 
        for enemies in self.entities: 
            enemies[1].move(False, 0.25, player=self.player)
            enemies[1].isAttackingPlayer(False)

    def add_enemy(self): 
        self.entities.clear()
        print(self.entities)
        for i in range(self.cal_wave()): 
            self.entities.append([0, EntityEnemy(100, 100, 800, 800, randrange(800), randrange(800))])
            print(self.entities)

    def get_enemies(self): 
        for enemy in self.entities: 
            return enemy[1]
