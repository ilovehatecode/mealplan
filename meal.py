import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

formatter = logging.Formatter('%(asctime)s:%(name)s:%(levelname)s:%(message)s')

file_handler = logging.FileHandler('meal.log')
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)
class Meal:

    def __init__(self, meal):
        self.meal = meal
        logger.info('Meal Created - {}'.format())

    def getMeal(self):
        return self.meal


    def getComponent(self, n):
        if n > len(self.meal) - 1:
            raise 'Out of range'
        elif type(n) != int:
            raise 'n not an integer'
        else:
            return self.meal[n]
            


    



    
