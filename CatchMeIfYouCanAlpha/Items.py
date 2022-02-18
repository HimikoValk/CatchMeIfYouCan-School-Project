import Item
from Main import Game, Main
class Chees(Item.ParentItem): 

    def __init__(self, item_x, item_y, item_desired_scale_x, item_desired_scale_y):
        super().__init__("Chees", "Data/Textures", item_x, item_y, item_desired_scale_x, item_desired_scale_y)
    
    def onAction(self, event):
         
        Game.player.set_speed(Game.player.speed * 1.25)
