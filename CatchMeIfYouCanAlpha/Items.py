from random import randrange
from Item import ParentItem

class ItemList(): 
    WIDTH = 800
    HEIGHT = 800
    def __init__(self):
        #Creating Object of Items´
        chees = Chees(randrange(self.WIDTH - 100), randrange(self.HEIGHT - 50))
        heart = Heart(randrange(self.WIDTH - 100), randrange(self.HEIGHT - 50), 80, 80)
        snowball = SnowBall(randrange(self.WIDTH), randrange(self.HEIGHT - 50), 80, 80)
        #Saving Items
        self.Items = [chees, heart, snowball]
        #self.Items.append(Chees)
        #Create Index for a random Item
        self.value = randrange(len(self.Items))

    def drawItems(self, screen): 
        for i in range(self.value): 
            self.Items[i].darw_item(screen)
     
        
    def handel_event(self, player): 
        for item in self.Items: 
            item.onAction(player)
        
    def get_item_by_name(self, item_name): 
        for i in range(0, len(self.Items)): 
            if self.Items[i].get_name() == item_name: 
                return self.Items[i]
            else: 
                return Exception()
    
    def calcualte_spawn_rate(self, wave, item): 
        return wave * 2 / item

class Chees(ParentItem): 

    onItem = False

    def __init__(self, item_x, item_y):
        super().__init__("Chees", "Data/Textures/Items/Chees.png", "Gives Player a higher Speed",item_x, item_y, 70, 70)
    
    def onAction(self, player):
        if(self.onItem == False): 
            if(player.player_sprite.rect.colliderect(self.item_sprite.rect)): 
                self.onItem = True
                player.set_speed(player.speed * 1.5)
                self.item_sprite.image.fill((0,0,0,0))
                self.item_sprite.remove()

class Heart(ParentItem): 

    IsOnItem = False

    def __init__(self, item_x, item_y, item_desired_scale_x, item_desired_scale_y):
        super().__init__("Heart", "Data/Textures/Items/Heart.png", "Healing Player",item_x, item_y, item_desired_scale_x, item_desired_scale_y)
    
    def onAction(self, player): 
        if(self.IsOnItem == False): 
            if(player.player_sprite.rect.colliderect(self.item_sprite.rect)): 
                self.IsOnItem = True
                if(player.hearts == 3): 
                    print("Max Hearts!")
                else: 
                     player.hearts +=1
                self.item_sprite.image.fill((0,0,0,0))
                self.item_sprite.remove()

class SnowBall(ParentItem): 

    IsOnItem = False

    def __init__(self, item_x, item_y, item_desired_scale_x, item_desired_scale_y):
        super().__init__("Snowball", "Data/Textures/Items/Snowball.png", "Damge Enemys or Kill them",item_x, item_y, item_desired_scale_x, item_desired_scale_y)
    
    def onAction(self, player): 
        if(self.IsOnItem == False): 
            if(player.player_sprite.rect.colliderect(self.item_sprite.rect)):
                self.IsOnItem = True
                self.item_sprite.image.fill((0,0,0,0))
                self.item_sprite.remove()
