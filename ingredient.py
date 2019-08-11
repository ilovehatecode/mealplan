from enum import Enum
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s:%(name)s:%(levelname)s:%(message)s')

##logging.basicConfig(filename='ingredient.log', level=logging.INFO, format='%(asctime)s:%(name)s:%(levelname)s:%(message)s')
file_handler = logging.FileHandler('ingredient.log')
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)

class IngredientType(Enum):
	VEGETABLE = 1
	FRUIT = 2
	GRAIN = 3
	BEANS = 4
	NUTS = 5
	MEAT = 6
	FISH = 7
	DAIRY = 8
	SEASONING = 9


class Ingredient:

        def __init__(self, ingred_name, ingred_type):
            self.name = str.upper(ingred_name)
            self.type = ingred_type.name
                      

            logger.info('Ingredient Created: {}'.format(ingred_name))
               
                        
                    
        def getIngredientType(self):
                return self.type

        def getIngredientName(self):
                return self.name


        

        
        
