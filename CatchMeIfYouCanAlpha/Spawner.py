from Player import Player
class Spwaner(): 

    def spawn_rate_cal(wave, player=Player):  # Cal = Calculation
        cal = player.speed * wave / 100 + player.hearts
        return cal
    


