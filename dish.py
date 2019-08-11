import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s:%(name)s:%(levelname)s:%(message)s')

file_handler = logging.FileHandler('dish.log')
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)

class Dish:

        def __init__(self, name, ingredients, recipe):
            self.recipe = recipe
            self.ingredients = ingredients
            self.name = name
            logger.debug('Created - {}'.format(name))



        def getIngredients(self):
                return self.ingredients

        def getRecipe(self):
                return self.recipe

        



        

        
        
