
class Meal:

    def __init__(self, meal):
        if type(meal) == list:
            self.meal = meal
        else:
            raise 'meal must be a list'

    def getMeal(self):
        return self.meal


    def getComponent(self, n):
        if n > len(self.meal) - 1:
            raise 'Out of range'
        elif type(n) != int:
            raise 'n not an integer'
        else:
            return self.meal[n]
            


    



    
