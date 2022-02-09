import time
from typing import final
import pygame
from pygame.constants import K_w
from pygame.constants import K_a
from pygame.constants import K_s
from pygame.constants import K_d
from DataBank import FireBaseDataBank
from Enemy import EntityEnemy
from InputBox import InputBox
from Player import Player

WIDTH, HEIGHT = 800, 800
#0 = Menu, 1 = game, 2 =  Quit
game_state = 0
wave = 1
score = 0

entites_alive = []


class Main(): 
    
    # db = DataBank
    #db.create_data(username='himiko', password="user123Fitrdf",score=0)
    #print(db.check_user_input_data("himiko", "user123Fitrdf")) 
    #db.update_user_score(username="himiko",score=20)

    def setup_pygame(title): 
        screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption(title)
        pygame.init()
        return screen
    
    def update_score(screen, font): 
        global score 
        score += 1
        score_text = font.render("SCORE: " + score, True, (74, 74, 74)) 
        #print(score_text)
        #screen.bilt(score_text, (WIDTH / 2, HEIGHT / 2))
    
    def menu(screen, font):
        global game_state

        COLOR = (217, 165, 76)
        Login_FONT = pygame.font.Font("Data/Fonts/Inter.ttf", 32)
        Regsiter_FONT = pygame.font.Font("Data/Fonts/Inter.ttf", 32)

        Check_text = "Waiting..."
        Check_Color = (255, 255, 255)

        login_text = Login_FONT.render("Login", True, (255, 255, 255))
        Register_text = Regsiter_FONT.render("Register", True, (255,255,255))

        username_text = ""
        password_text = ""
        register_username_text = ""
        register_password_text = ""
        
        username_input_box = InputBox(WIDTH / 2 - 100, 100, 140, 32, font, "username", username_text)
        password_input_box = InputBox(WIDTH / 2 - 100, 150, 140, 32, font, "password", password_text)
        rusername_input_box = InputBox(WIDTH / 2 - 100, 400, 140, 32, font, "username", register_username_text)
        rpassword_input_box = InputBox(WIDTH / 2 - 100, 450, 140, 32, font, "password", register_password_text)

        input_boxes = [username_input_box, password_input_box, rusername_input_box, rpassword_input_box]

        
        while game_state == 0: 
            screen.fill(COLOR)
            screen.blit(login_text, (WIDTH / 2 - login_text.get_width() / 2, 0))
            screen.blit(Register_text, (WIDTH / 2 - Register_text.get_width() / 2, 300))
            screen.blit(font.render("Username:", True, (255, 255, 255)), (WIDTH / 2 - 200, 100))
            screen.blit(font.render("Password:", True, (255, 255, 255)), (WIDTH / 2 - 200, 150))
            
            screen.blit(font.render("Username:", True, (255, 255, 255)), (WIDTH / 2 - 200, 400))
            screen.blit(font.render("Password:", True, (255, 255, 255)), (WIDTH / 2 - 200, 450))         

            screen.blit(font.render(Check_text, True, Check_Color), (WIDTH / 2 - 100, 200))

            for event in pygame.event.get():  
                if(event.type == pygame.QUIT): 
                    game_state = 2  
                for box in input_boxes: 
                    box.handel_event(event)
                if event.type == pygame.KEYDOWN: 
                    if event.key == pygame.K_RETURN: 
                        if(username_text == "" and password_text == ""): 
                            if(register_username_text != "" and register_password_text != ""): 
                                FireBaseDataBank().create_user(username=register_username_text, password=register_password_text, score=0)
                        
                        if(username_text != "" and  password_text != ""): 
                            if(FireBaseDataBank().check_user_input_data(username_input_box.get_text(), password_input_box.get_text()) == True): 
                                Check_text = "Login was Successfully!"
                                Check_Color = (70, 173, 2)
                            else:
                                Check_text = "Username or Password isn't Correct!"
                                Check_Color = (247, 0, 0)                            

            for box in input_boxes: 
                box.update()
                box.draw(screen)
            
            pygame.display.update()
            
                


        
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
       
        clock = pygame.time.Clock()
        keys = [False, False, False, False]
        player = Player(80, 80, WIDTH, HEIGHT)
        

        while(game_state == 1): 
            screen.fill((255, 255, 255))
            for event in pygame.event.get(): 
                if(event.type == pygame.QUIT): 
                    game_state = 2
                #print(event)
                self.handle_inputs(keys, event)
            player.move(keys, 1)
            player.draw(screen)
            #enemy.draw(screen)
            #Main.update_score(screen, font)
            
            pygame.display.update()
            clock.tick(144)

       
    
    def __init__(self):
        db = FireBaseDataBank() 
        global game_state
        global score
        global entites_alive
        game_state = 0

        db.establish()
        #print(db.check_user_input_data("himiko", "user123Fitrdf"))
        
        while game_state != 2: 
            screen = Main.setup_pygame("Catch Me if you can")
            font = pygame.font.Font("Data/Fonts/Inter.ttf", 16)
            self.previous_frame_time = time.time()
            Main.menu(screen, font)
            #self.run_game(screen, font)
            

game = Game()
        
        


        
    