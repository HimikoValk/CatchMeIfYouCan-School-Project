import pygame


class ParentItem(): 
    
    position = pygame.Vector2()
    scale = 0

    def __init__(self, item_name, item_texture, item_x, item_y, item_desired_scale_x, item_desired_scale_y):
        
        self.item_name = item_name

        self.item_sprite = pygame.sprite.Sprite()
        self.item_sprite.image = pygame.image.load(item_texture)
        self.item_sprite.rect = self.item_sprite.image.get_rect()
        self.item_sprite.image = pygame.transform.scale(self.item_sprite.image, (int(self.item_x), int(self.item_y)))

        self.scale.x = item_desired_scale_x
        self.scale.y = item_desired_scale_y

        self.item_x = item_x
        self.item_y = item_y

        self.position.x = item_x
        self.position.y = item_y
    
    def darw_item(self, screen): 
        img_copy = pygame.transform.scale(self.item_sprite.image, (int(self.scale), int(self.scale)))
        screen.blit(img_copy, (self.position.x - int(img_copy.get_width() / 2), self.position.y - int(img_copy.get_heigh() / 2)))
