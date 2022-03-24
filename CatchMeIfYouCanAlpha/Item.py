import pygame

class ParentItem(): 
    
    position = pygame.Vector2()
    scale = pygame.Vector2()

    def __init__(self, item_name, item_texture, item_description,item_x, item_y, item_desired_scale_x, item_desired_scale_y):
        
        self.item_name = item_name
        self.item_description = item_description

        self.scale.x = item_desired_scale_x
        self.scale.y = item_desired_scale_y

        self.position.x = item_x
        self.position.y = item_y

        self.item_sprite = pygame.sprite.Sprite()
        self.item_sprite.image = pygame.image.load(item_texture)
        self.item_sprite.image = pygame.transform.scale(self.item_sprite.image, (int(self.scale.x), int(self.scale.y)))
        self.item_sprite.rect = self.item_sprite.image.get_rect()
        self.item_sprite.rect.center = self.position.x, self.position.y
    
    def darw_item(self, screen): 
        screen.blit(self.item_sprite.image, (self.item_sprite.rect.x, self.item_sprite.rect.y))

    def draw_item_rect(self, screen, texture_rect): 
        pygame.draw.rect(screen, 'Red', texture_rect, 2)

    def get_name(self): 
        return self.item_name
    