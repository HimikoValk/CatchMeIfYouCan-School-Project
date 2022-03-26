from threading import Thread
import pygame
from random import seed 
from random import randint
from Player import Player
from Spawner import Spwaner
from random import randrange


class EntityEnemy(object): 
    WHIDTH, HEIGHT = 800, 800
    global game_state
    global entities_alive


    #Tranform 
    position = pygame.Vector2() 
    scale = pygame.Vector2()

    #Physics
    speed = 250

    #Graphics
    enemy_sprite = 0
    rotaion = 0
    rot_speed = 30  #30-40
    animations = [pygame.image.load("Data/Textures/Cat/Run (1).png"), pygame.image.load("Data/Textures/Cat/Run (2).png"), pygame.image.load("Data/Textures/Cat/Run (3).png"), pygame.image.load("Data/Textures/Cat/Run (4).png"), pygame.image.load("Data/Textures/Cat/Run (5).png"), pygame.image.load("Data/Textures/Cat/Run (6).png"), pygame.image.load("Data/Textures/Cat/Run (7).png")]

    #utils
    move_way = [False, False, False, False]
    animation_state = 0
    attack_player = False

    
    def __init__(self, desired_scale_x, desired_scale_y, Width, Height, posX, posY):
        self.scale.x = desired_scale_x
        self.scale.y = desired_scale_y

        self.scalar = 50

        self.enemy_sprite = pygame.sprite.Sprite()
        self.enemy_sprite.image = self.animations[self.animation_state].convert_alpha()
        self.enemy_sprite.image = pygame.transform.scale(self.enemy_sprite.image, (int(self.scale.x), int(self.scale.y)))
        self.enemy_sprite.rect = self.enemy_sprite.image.get_rect()


        self.position.x = posX
        self.position.y = posY

        self.enemy_sprite.rect.width /=2
        self.enemy_sprite.rect.height /= 2

        self.scalar = self.scale.x

    def move(self, attack_player, dt, player=Player): 
        self.attack_player = attack_player
        if(self.attack_player == True): 
            self.handel_move_way(dt, player=player)
            if(self.enemy_sprite.rect.colliderect(player.player_sprite.rect)): 
                player.hearts -= 1
                print("You Lost a heart!" + str(player.hearts))
                #pygame.time.delay(5)
        else: 
            self.enemy_sprite.image.fill((0,0,0,0))
            self.enemy_sprite.kill()
            self.enemy_sprite.remove()


        '''
        if(attack_player == False):
            if(player.position.x != self.position.x and player.position.y != self.position.y or not self.enemy_sprite.rect.colliderect(player.player_sprite.rect)): 
                if(player.position.x < self.position.x): 
                    self.handel_move_way(1, dt)
                elif(player.position.x > self.position.x): 
                    self.handel_move_way(3, dt)
                elif(player.position.y < self.position.y): 
                    self.handel_move_way(0, dt)
                elif(player.position.y > self.position.y): 
                    self.handel_move_way(2, dt)
        '''
            


    def handel_move_way(self, dt, player=Player): 
        
        if(self.position.y <= 0): 
            self.position.y += 4
        elif(self.position.y >= 800): 
            self.position.y -= 4
        elif(self.position.x <= 0): 
            self.position.x += 4
        elif(self.position.x >= 800): 
            self.position.x -= 4

        if(self.position.x <= player.position.x): 
                self.move_way[3] = True
        else: 
            self.move_way[3] = False 
        if(self.position.x >= player.position.x): 
                self.move_way[1] = True
        else: 
            self.move_way[1] = False
        if(self.position.y <= player.position.y): 
                self.move_way[2] = True
        else: 
            self.move_way[2] = False
        if(self.position.y >= player.position.y): 
                self.move_way[0] = True
        else:
            self.move_way[0] = False
        
        if(self.move_way[0]):
            self.position.y -= 0.01 * dt * self.speed
            self.rotaion += 0.01 * dt * self.rot_speed
            self.animation_state += 0.05
            if(self.animation_state >= len(self.animations)): 
                self.animation_state = 0
            #self.enemy_sprite.image = pygame.image.load(self.animations[int(self.animation_state)]).convert_alpha()
        else: 
            self.move_way[0] = False

        if(self.move_way[1]):
            self.position.x -= 0.01 * dt * self.speed
            self.rotaion += 0.01 * dt * self.rot_speed
            self.animation_state += 0.05
            if(self.animation_state >= len(self.animations)): 
                self.animation_state = 0
            #self.enemy_sprite.image = pygame.image.load(self.animations[int(self.animation_state)]).convert_alpha()          
        else: 
            self.move_way[1] = False        

        if(self.move_way[2]):
            self.position.y += 0.01 * dt * self.speed
            self.rotaion -= 0.01 * dt * self.rot_speed
            self.animation_state += 0.05
            if(self.animation_state >= len(self.animations)): 
                self.animation_state = 0
            #self.enemy_sprite.image = pygame.image.load(self.animations[int(self.animation_state)]).convert_alpha()
        else: 
            self.move_way[2] = False

        if(self.move_way[3]): 
            self.position.x += 0.01 * dt * self.speed
            self.rotaion -= 0.01 * dt * self.rot_speed
            self.animation_state += 0.05
            if(self.animation_state >= len(self.animations)): 
                self.animation_state = 0
            #self.enemy_sprite.image = pygame.image.load(self.animations[int(self.animation_state)]).convert_alpha()
            
        else: 
            self.move_way[3] = False

        self.enemy_sprite.rect.center = self.position.x, self.position.y       

    def isAttackingPlayer(self, attack_player): 
        self.attack_player = attack_player
        return self.attack_player

    def draw(self,screen):

        spawner_calcs = 0
        if(spawner_calcs != 0):
            pass
        else: 
            img_copy = pygame.transform.scale(self.enemy_sprite.image, (int(self.scale.x), int(self.scale.y)))
            img_copy = pygame.transform.rotate(img_copy, self.rotaion)
            screen.blit(img_copy, (self.position.x - int(img_copy.get_width() / 2), self.position.y - int(img_copy.get_height() / 2)))
    def draw_rect(self, screen): 
        pygame.draw.rect(screen, 'Red', self.enemy_sprite.rect, 2)


    