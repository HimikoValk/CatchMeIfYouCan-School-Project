import time
from typing import final
from threading import Thread
import pygame
from pygame.constants import K_w
from pygame.constants import K_a
from pygame.constants import K_s
from pygame.constants import K_d
from Button import Button
from DataBank import FireBaseDataBank
from Enemy import EntityEnemy
from InputBox import InputBox
from Player import Player

WIDTH, HEIGHT = 800, 800
username = ""
#0 = Menu, 1 = RegisterMenu, 2 = game, 3 =  Quit
game_state = 0
wave = 1
score = 0

entites_alive = []


class Main(): 
    
    db = FireBaseDataBank()
    #db.create_user(username='rds', password="user123Fitrdf",score=0)
    #print(db.check_user_input_data("himiko", "user123Fitrdf")) 
    #db.update_user_score(username="himiko",score=20)

    def setup_pygame(title): 
        screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption(title)
        pygame.init()
        return screen
    
    
    def login_menu(screen, font):
        global username 
        global game_state

        COLOR = (217, 165, 76)
        Login_FONT = pygame.font.Font("Data/Fonts/Inter.ttf", 32)

        Check_text = "Waiting..."
        Check_Color = (255, 255, 255)

        login_text = Login_FONT.render("Login", True, (255, 255, 255))

        username_text = ""
        password_text = ""
        
        username_input_box = InputBox(WIDTH / 2 - 100, 100, 140, 32, font, "username", username_text)
        password_input_box = InputBox(WIDTH / 2 - 100, 150, 140, 32, font, "password", password_text)

        login_button = Button(WIDTH / 2 - 150, 200, 140, 32, (255, 255, 255), font, "Login")
        register_button = Button(WIDTH / 2 , 200, 140, 32, (255, 255, 255), font, "Register")

        input_boxes = [username_input_box, password_input_box]
        buttons = [login_button, register_button]

        
        while game_state == 0: 
            screen.fill(COLOR)
            screen.blit(login_text, (WIDTH / 2 - login_text.get_width() / 2, 0))
            screen.blit(font.render("Username:", True, (255, 255, 255)), (WIDTH / 2 - 200, 100))
            screen.blit(font.render("Password:", True, (255, 255, 255)), (WIDTH / 2 - 200, 150))

            screen.blit(font.render(Check_text, True, Check_Color), (WIDTH / 2 - len(Check_text) - 100 , 300))

            for event in pygame.event.get():  
                if(event.type == pygame.QUIT): 
                    game_state = 3 
                     
                for box in input_boxes: 
                    box.handel_event(event)
                
                for button in buttons: 
                    button.handel_event(event)
                    
                    if(buttons[1].active):
                        game_state = 1
                    
                    elif(buttons[0].active): 
                        if(FireBaseDataBank().check_user_input_data(username_input_box.get_text(), password_input_box.get_text()) == True): 
                            username = username_input_box.get_text()
                            Check_text = "Login was Successfully!"
                            Check_Color = (70, 173, 2)
                            game_state = 2
                        else:
                            Check_text = "Username or Password isn't Correct!"
                            Check_Color = (247, 0, 0)                          

                        
            for button in buttons: 
                button.draw(screen)

            for box in input_boxes: 
                box.update()
                box.draw(screen)
            
            pygame.display.update()

    def register_menu(screen, font): 
        global game_state

        COLOR = (217, 165, 76)
        Regsiter_FONT = pygame.font.Font("Data/Fonts/Inter.ttf", 32)
        REGISTER_TEXT = Regsiter_FONT.render("Register", True, (255, 255, 255))

        register_button = Button(WIDTH / 2 - 150 , 200, 140, 32, (255, 255, 255), font, "Register")
        back_to_login = Button(WIDTH / 2 , 200, 140, 32, (255, 255, 255), font, "Back to Login")
        
        username_text = ""
        password_text = ""

        username_input_box = InputBox(WIDTH / 2 - 100, 100, 140, 32, font, "username", username_text)
        password_input_box = InputBox(WIDTH / 2 - 100, 150, 140, 32, font, "password", password_text)
        input_boxes = [username_input_box, password_input_box]
        buttons = [register_button, back_to_login]
        
        while game_state == 1: 
            screen.fill(COLOR)
            screen.blit(REGISTER_TEXT, (WIDTH / 2 - REGISTER_TEXT.get_width() / 2 , 0))
            screen.blit(font.render("Username:", True, (255, 255, 255)), (WIDTH / 2 - 200, 100))
            screen.blit(font.render("Password:", True, (255, 255, 255)), (WIDTH / 2 - 200, 150))

            for event in pygame.event.get(): 
                if(event.type == pygame.QUIT): 
                    game_state = 3

                for button in buttons: 
                    button.handel_event(event)

                for box in input_boxes: 
                    box.handel_event(event)
                    
                    if(buttons[0].active): 
                        if(FireBaseDataBank().create_user(username_input_box.get_text(), password_input_box.get_text(), 0)):
                            buttons[0].active = False
                    if(buttons[1].active): 
                        game_state = 0
            
            for button in buttons: 
                button.draw(screen)

            for box in input_boxes: 
                box.update() 
                box.draw(screen) 

            pygame.display.update()


             
class Game(): 

    player = Player(80, 80, WIDTH, HEIGHT)

    def update_score(self): 
        global score
        #pygame.time.delay(1000)
        score += 1

    def run_game(self, screen, font):
        global game_state
        global username
        global score
       
        color = (0, 0, 0)
        text = "Score:"
        clock = pygame.time.Clock()
        keys = [False, False, False, False]
        self.player = Player(80, 80, WIDTH, HEIGHT)
        enemy = EntityEnemy(80, 80, WIDTH, HEIGHT)        
        highscore = 0
        
        #Fixed Program Crash in register menu
        if(game_state == 2):
            highscore = FireBaseDataBank().get_score(username)

        while(game_state == 2): 
            
            #print(FireBaseDataBank().get_score(username))
            screen.fill((255, 255, 255))
            if(score > highscore): 
                color = (50, 168, 82)
                text = "New HighScore! Score:" 
                highscore = score

            screen.blit(font.render(text + str(score), True , color), (WIDTH / 2  - 100 , 0))
            screen.blit(font.render("HighScore:" + str(highscore), True , (0, 0, 0)), (0, 0))
            for event in pygame.event.get(): 
                if(event.type == pygame.QUIT): 
                    FireBaseDataBank().update_user_score(username=username, score=score)
                    game_state = 3
                self.player.handle_inputs(keys, event)
            self.player.move(keys, 0.5)
            self.player.draw(screen)
            enemy.move(False, 0.45)
            enemy.draw(screen)
            self.update_score()
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
        
        while game_state != 3: 
            screen = Main.setup_pygame("Catch Me if you can")
            font = pygame.font.Font("Data/Fonts/Inter.ttf", 16)
            self.previous_frame_time = time.time()
            Main.login_menu(screen, font)
            Main.register_menu(screen, font)
            self.run_game(screen, font)
    
    def get_player_speed(self): 
        return self.player
            
game = Game()