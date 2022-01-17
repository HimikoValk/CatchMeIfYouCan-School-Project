import pygame

class Entity(): 
    
    entityTags = [
        "Player", 
        "Enemy",
        ]

    entityDefaultValue = 0

    def __int__(self): 
        self.entityTags[self.entityDefaultValue]

    def getEntityTagByName(self, entityTagName): 
        for entityTagName in self.entityTags: 
            if entityTagName == self.entityTags: 
                return entityTagName

