import time
from typing import final
import pygame
from pygame.constants import K_w
from pygame.constants import K_a
from pygame.constants import K_s
from pygame.constants import K_d
from DataBank import FireBaseDataBank
from Enemy import EntityEnemy
from Player import Player

WIDTH, HEIGHT = 800, 800
#0 = Menu, 1 = game, 2 =  Quit
game_state = 0
wave = 1
score = 0

entites_alive = []


class Main(): 

    # db = DataBank
    db = FireBaseDataBank() 
    db.establish() 
    #db.create_data(username='himiko', password="user123Fitrdf",score=0)
    user = db.get_ref("himiko")
    #print(db.check_user_input_data("himiko", "user123Fitrdf")) 
    #db.update_user_score(username="himiko",score=20)

    
    def setup_pygame(title): 
        screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption(title)
        pygame.init()
        return screen
    
    def update_score(screen, text): 
        global score 
        score += 1
        score_text = text.render("SCORE: " + str(score), True, (0,0,0)) 
        #print(score_text)
        '''
        score_rect = score_text.get_rect(center=(400, 400))
        screen.bilt(score_text, score_rect)
        '''
        
class Game(): 
    def handle_inputs(self, keys, event): 
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

    def run_game(self, screen, font):
        global game_state
        WHITE = (255, 255, 255)
        clock = pygame.time.Clock()
        keys = [False, False, False, False]
        player = Player(80, 80, WIDTH, HEIGHT)
        enemy = EntityEnemy(80, 80, WIDTH, HEIGHT)
        

        while(game_state == 1): 
            screen.fill(WHITE)
            for event in pygame.event.get(): 
                if(event.type == pygame.QUIT): 
                    game_state = 2
                print(event)
                self.handle_inputs(keys, event)
            enemy.move(True, 1)
            #player.move(keys, 1)
            #player.draw(screen)
            enemy.draw(screen)
            Main.update_score(screen, font)
            
            pygame.display.update()
            clock.tick(144)

       
    
    def __init__(self):
        global game_state
        global score
        global entites_alive

        game_state = 1
        
        while game_state != 2: 
            screen = Main.setup_pygame("Catch Me if you can")
            font = pygame.font.Font("Data/Fonts/Inter.ttf", 32)
            self.previous_frame_time = time.time()
            self.run_game(screen, font)
            

game = Game()
        
        


        
    