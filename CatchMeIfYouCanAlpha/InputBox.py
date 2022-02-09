import pygame
from DataBank import FireBaseDataBank
class InputBox: 

    def __init__(self, x ,y , width, height, font, category,text=''):
        self.rect =  pygame.Rect(x, y , width, height)
        self.color = (255, 255, 255)
        self.text = text
        self.text_surface = font.render(text, True, self.color)
        self.active = False
        self.font = font
        self.category = category
    
    def handel_event(self, event): 
        if event.type == pygame.MOUSEBUTTONDOWN: 
            if self.rect.collidepoint(event.pos): 
                self.active = True
            else: 
                self.active = False


        if event.type == pygame.KEYDOWN: 
            if self.active: 
                if event.key == pygame.K_RETURN:
                    print(f"{self.category}: {self.text}")
                elif event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode
                # Re-render the text.
                self.text_surface = self.font.render(self.text, True, self.color)

    def get_text(self): 
        return self.text

    def update(self): 
        # Updating rect width
        width = max(200, self.text_surface.get_width() + 10)
        self.rect.w = width

    def draw(self, screen): 
       # Blit the text.
        screen.blit(self.text_surface, (self.rect.x+5, self.rect.y+5))
        # Blit the rect.
        pygame.draw.rect(screen, self.color, self.rect, 2)        