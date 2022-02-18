import pygame
class Button(): 

    def __init__(self, x, y, width, height, color, font,text=""):
        self.rect = pygame.Rect(x, y, width, height)
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.font = font
        self.text = text
        self.active = False
    
    def draw(self, screen): 

        pygame.draw.rect(screen, self.color, self.rect, 0)

        if self.text != "": 
            text = self.font.render(self.text, 1, (0,0,0))
            screen.blit(text, (self.x + (self.width/2 - text.get_width() / 2), self.y + (self.height / 2 - text.get_height() / 2 )))
    
    def handel_event(self, event): 
        if event.type == pygame.MOUSEBUTTONDOWN: 
            if self.rect.collidepoint(event.pos): 
                self.active = True
            else: 
                self.active = False
        
    def is_active(self): 
        return self.active