from threading import Thread
import pygame
from random import seed 
from random import randint
from Spawner import Spwaner


class EntityEnemy(): 
    global game_state
    global entities_alive

    #Tranform 
    position = pygame.Vector2() 
    scale = pygame.Vector2()

    #Physics
    speed = 300

    #Graphics
    enemy_sprite = 0
    rotaion = 0
    rot_speed = 30  #30-40

    #utils
    move_way = [False, False, False, False]

    
    def __init__(self, desired_scale_x, desired_scale_y, Width, Height):
        self.scale.x = desired_scale_x
        self.scale.y = desired_scale_y

        self.scalar = 50

        self.enemy_sprite = pygame.sprite.Sprite()
        self.enemy_sprite.image = pygame.image.load("Data/Textures/MobTexture1.png").convert_alpha()
        self.enemy_sprite.rect = self.enemy_sprite.image.get_rect()
        self.enemy_sprite.image = pygame.transform.scale(self.enemy_sprite.image, (int(self.scale.x), int(self.scale.y)))

        self.position.x = Width / 2
        self.position.y = Height / 2 

        self.scalar = self.scale.x

    def move(self,attack_player, dt): 
        if(attack_player == False): 
            value = randint(0, 3)
            self.handel_move_way(0, dt)        


    def handel_move_way(self, index, dt): 
        self.move_way[index]
        
        if(self.move_way[0]):
            self.position.y -= 0.01 * dt * self.speed
            self.rotation += 0.01 * dt * self.rot_speed

        if(self.move_way[1]):
            self.position.x -= 0.01 * dt * self.speed
            self.rotation += 0.01 * dt * self.rot_speed

        if(self.move_way[2]):
            self.position.y += 0.01 * dt * self.speed
            self.rotation -= 0.01 * dt * self.rot_speed
        if(self.move_way[3]): 
            self.position.x += 0.01 * dt * self.speed
            self.rotation -= 0.01 * dt * self.rot_speed

        self.enemy_sprite.rect.topleft = self.position.x, self.position.y       

    def draw(self,screen):

        spawner_calcs = 0
        if(spawner_calcs == 1):
            pass
        else: 
            spawner_calcs += 1
            spawnerCalc_value = int(Spwaner.spawn_rate_cal())
            img_copy = pygame.transform.scale(self.enemy_sprite.image, (int(self.scalar), int(self.scalar)))
            img_copy = pygame.transform.rotate(img_copy, self.rotaion)
            screen.blit(img_copy, (self.position.x - int(img_copy.get_width() / 2), self.position.y - int(img_copy.get_height() / 2)))


    