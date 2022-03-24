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

class Player():
    global game_state
    hearts = 3
    animtion_satte = 0
    
    #Transform
    position = pygame.Vector2()
    scale = pygame.Vector2()
    rotated = 0

    #Physics
    velocity_y = 0
    gravity_scale = 3000
    speed = 350

    #Graphics
    player_sprite = 0
    rotation = 0
    rot_speed = 30
    animations = ["Data/Textures/PlayerTexture1.png", "Data/Textures/PlayerTexture2.png", "Data/Textures/PlayerTexture3.png", "Data/Textures/PlayerTexture4.png"]

    def __init__(self, desired_scale_x, desired_scale_y, Width, Height):
        self.scale.x = desired_scale_x
        self.scale.y = desired_scale_y

        self.scalar = 50

        self.player_sprite = pygame.sprite.Sprite()
        self.player_sprite.image = pygame.image.load(self.animations[self.animtion_satte]).convert_alpha()
        self.player_sprite.image = pygame.transform.scale(self.player_sprite.image, (int(self.scale.x), int(self.scale.y)))
        self.player_sprite.rect = self.player_sprite.image.get_rect()

        self.position.x = Width / 2
        self.position.y = Height / 2 

        self.scalar = self.scale.x

        self.width = Width
        self.height = Height


    def move(self, keys, dt): 
        global score_int
        global score

        if(self.position.y <= 0): 
            self.position.y += 4
        elif(self.position.y >= 800): 
            self.position.y -= 4
        elif(self.position.x <= 0): 
            self.position.x += 4
        elif(self.position.x >= 800): 
            self.position.x -= 4

        if(keys[0]):
            self.position.y -= 0.01 * dt * self.speed
            self.rotation += 0.04 * dt * self.rot_speed
            self.animtion_satte += 0.04
            if(self.animtion_satte >= len(self.animations)): 
                self.animtion_satte = 0
            self.player_sprite.image = pygame.image.load(self.animations[int(self.animtion_satte)]).convert_alpha()
            
        if(keys[1]):
            self.position.x -= 0.01 * dt * self.speed
            self.rotation += 0.04 * dt * self.rot_speed
            self.animtion_satte += 0.04
            if(self.animtion_satte >= len(self.animations)): 
                self.animtion_satte = 0
            self.player_sprite.image = pygame.image.load(self.animations[int(self.animtion_satte)]).convert_alpha()

        if(keys[2]):
            self.position.y += 0.01 * dt * self.speed
            self.rotation -= 0.04 * dt * self.rot_speed
            self.animtion_satte += 0.04
            if(self.animtion_satte >= len(self.animations)): 
                self.animtion_satte = 0
            self.player_sprite.image = pygame.image.load(self.animations[int(self.animtion_satte)]).convert_alpha()

        if(keys[3]): 
            self.position.x += 0.01 * dt * self.speed
            self.rotation -= 0.04 * dt * self.rot_speed
            self.animtion_satte += 0.04
            if(self.animtion_satte >= len(self.animations)): 
                self.animtion_satte = 0
            self.player_sprite.image = pygame.image.load(self.animations[int(self.animtion_satte)]).convert_alpha()
            #self.player_sprite.image = pygame.image.load(self.animations[int(self.animtion_satte)]).convert_alpha()
        

        #self.velocity_y += 0.00001 * dt * self.gravity_scale

        #self.position.y += self.velocity_y * dt

        self.player_sprite.rect.center = self.position.x, self.position.y

    def draw(self, screen):
        img_copy = pygame.transform.scale(self.player_sprite.image, (int(self.scale.x), int(self.scale.y)))
        img_copy = pygame.transform.rotate(img_copy, self.rotation)
        screen.blit(img_copy, (self.position.x - int(img_copy.get_width() / 2), self.position.y - int(img_copy.get_height() / 2)))

    def handle_inputs(self,keys, event): 
        if(event.type == pygame.KEYDOWN): 
            if(event.key == K_w): 
                keys[0] = True
            if(event.key == K_a): 
                keys[1] = True
            if(event.key == K_s): 
                keys[2] = True
            if(event.key == K_d): 
                keys[3] = True

        if(event.type == pygame.KEYUP): 
            if(event.key == K_w): 
                keys[0] = False
            if(event.key == K_a): 
                keys[1] = False
            if(event.key == K_s): 
                keys[2] = False
            if(event.key == K_d): 
                keys[3] = False   
    
    def set_speed(self, speed): 
        self.speed = speed

    def get_speed(self): 
        return self.speed