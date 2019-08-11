from ingredient import Ingredient, IngredientType
from dish import Dish
from meal import Meal
import logging

logging.basicConfig(filename='test.log', level=logging.DEBUG, format='%(asctime)s:%(name)s:%(levelname)s:%(message)s')

grnPepper = Ingredient('green pepper', IngredientType.VEGETABLE)
banana = Ingredient('banana', IngredientType.FRUIT)
strawberry = Ingredient('strawberry', IngredientType.FRUIT)

spinach = Ingredient('spinach', IngredientType.VEGETABLE)


sampleDish1 = Dish('', [grnPepper, spinach], 'Cut 4oz of spinach and 1 oz of green pepprs. Place in pot with 16oz of water. Boil for one hour. Serve')
sampleDish2 = Dish('Dish 2', [strawberry, banana], 'Cut 4oz of strawberries and 2 oz of bananas. Place in bowl and toss.')

sampleMeal = Meal('[sampleDish1, sampleDish2, banana]')

logging.debug(sampleMeal.getMeal())






    
