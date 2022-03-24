import DataBank
class SList(): 
    dataBank = DataBank.FireBaseDataBank()
    scorelist = []

    def __init__(self):
        for username in self.dataBank.useres_ref():
            self.scorelist.append(self.dataBank.get_ref(username)) 
    
