from random import randrange
from secrets import randbelow
import pygame
from Enemy import EntityEnemy

from Player import Player


class BackGround(): 
    
    
    #Transform
    position = pygame.Vector2()
    scale = pygame.Vector2()

    #Graphics
    tree_sprite = 0



    def __init__(self, desired_scale_x, desired_scale_y, x, y):
        self.back_ground = pygame.image.load("Data/Textures/GameMap.png").convert_alpha()
        self.scale.x = desired_scale_x
        self.scale.y = desired_scale_y
        self.tree_sprite = pygame.sprite.Sprite()
        self.tree_sprite.image  = pygame.image.load("Data/Textures/Tree.png").convert_alpha()
        self.tree_sprite.rect = self.tree_sprite.image.get_rect()
        self.tree_sprite.image = pygame.transform.scale(self.tree_sprite.image, (int(self.scale.x), int(self.scale.y)))
        self.position.x = x
        self.position.y = y
        self.tree_sprite.rect.center = self.position.x, self.position.y 
        self.tree_sprite.rect.height /= 2
        self.tree_sprite.rect.width /= 2
        self.tree_sprite.rect.x += 90 
        self.tree_sprite.rect.y += 100 

        self.value_of_trees = randrange(10)

    def drawBackGround(self, screen): 
        img_scale = pygame.transform.scale(self.back_ground, (self.back_ground.get_width(), 800))
        screen.blit(img_scale, (0, 0))
    
    def drawTree(self, screen, player=Player, enemy=EntityEnemy):
        screen.blit(self.tree_sprite.image, (self.position.x, self.position.y))
        if(player.player_sprite.rect.colliderect(self.tree_sprite.rect)): 
                player.position.x -=2
        elif(enemy.enemy_sprite.rect.colliderect(self.tree_sprite.rect)): 
                enemy.position.x -= 2

    def draw_rect(self, screen): 
        pygame.draw.rect(screen, 'Red', self.tree_sprite.rect, 2)
