import pygame
from pygame.locals import *
from pygame.math import Vector2
from pygame import mixer
import time
import random
import math

#0 = Menu, 1 = Game, 2 = Quit
game_state = 0
score = 0
score_int = 0


entities_alive = []

class Player():
    global game_state
    hearts = 3
    
    #Transform
    position = pygame.Vector2()
    scale = pygame.Vector2()

    #Physics
    velocity_y = 0
    gravity_scale = 3000
    speed = 350

    #Graphics
    player_sprite = 0
    rotation = 0
    rot_speed = 30



    def __init__(self, desired_scale_x, desired_scale_y, Width, Height):
        self.scale.x = desired_scale_x
        self.scale.y = desired_scale_y

        self.scalar = 50

        self.player_sprite = pygame.sprite.Sprite()
        self.player_sprite.image = pygame.image.load("Data/Textures/MobTexture1.png").convert_alpha()
        self.player_sprite.rect = self.player_sprite.image.get_rect()
        self.player_sprite.image = pygame.transform.scale(self.player_sprite.image, (int(self.scale.x), int(self.scale.y)))

        self.position.x = Width / 2
        self.position.y = Height / 2 

        self.scalar = self.scale.x

    def move(self, keys, dt): # dt = wave_speed gettig bigger by wave
        global score_int
        global score
        global max_score

        if(keys[0]):
            self.position.y -= 0.01 * dt * self.speed
            if(self.rotation != 0):
                self.rotation += 0.01 * dt * self.rot_speed
            else:
                self.rotation = 0
        if(keys[1]):
            self.position.x -= 0.01 * dt * self.speed
            self.rotation += 0.01 * dt * self.rot_speed

        if(keys[2]):
            self.position.y += 0.01 * dt * self.speed
            self.rotation -= 0.01 * dt * self.rot_speed
        if(keys[3]): 
            self.position.x += 0.01 * dt * self.speed
            self.rotation -= 0.01 * dt * self.rot_speed

        #self.velocity_y += 0.00001 * dt * self.gravity_scale

        #self.position.y += self.velocity_y * dt

        self.player_sprite.rect.topleft = self.position.x, self.position.y

    def draw(self, screen, colliders):
        img_copy = pygame.transform.scale(self.player_sprite.image, (int(self.scalar), int(self.scalar)))
        img_copy = pygame.transform.rotate(img_copy, self.rotation)
        screen.blit(img_copy, (self.position.x - int(img_copy.get_width() / 2), self.position.y - int(img_copy.get_height() / 2)))