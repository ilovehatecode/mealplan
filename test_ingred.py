##Unit Testing
import unittest
##Import module to test
from ingredient import Ingredient, IngredientType

class TestIngredient(unittest.TestCase):

    def test_ingredientname(self):
        ingredient_1 = Ingredient('green pepper', IngredientType.VEGETABLE)
        ingredient_2 = Ingredient('green apple', IngredientType.FRUIT)
        ingredient_3 = Ingredient('peanuts', IngredientType.NUTS)
        ingredient_4 = Ingredient('bread', IngredientType.GRAIN)
        ingredient_5 = Ingredient('pinto beans', IngredientType.BEANS)
        ingredient_6 = Ingredient('steak', IngredientType.MEAT)
        ingredient_7 = Ingredient('salmon', IngredientType.FISH)
        ingredient_8 = Ingredient('milk', IngredientType.DAIRY)
        ingredient_9 = Ingredient('oregano', IngredientType.SEASONING)

        self.assertEqual(ingredient_1.getIngredientName(), 'GREEN PEPPER')
        self.assertEqual(ingredient_2.getIngredientName(), 'GREEN APPLE')
        self.assertEqual(ingredient_3.getIngredientName(), 'PEANUTS')
        self.assertEqual(ingredient_4.getIngredientName(), 'BREAD')
        self.assertEqual(ingredient_5.getIngredientName(), 'PINTO BEANS')
        self.assertEqual(ingredient_6.getIngredientName(), 'STEAK')
        self.assertEqual(ingredient_7.getIngredientName(), 'SALMON')
        self.assertEqual(ingredient_8.getIngredientName(), 'MILK')
        self.assertEqual(ingredient_9.getIngredientName(), 'OREGANO')

    def test_ingredienttype(self):
        ingredient_1 = Ingredient('green pepper', IngredientType.VEGETABLE)
        ingredient_2 = Ingredient('green apple', IngredientType.FRUIT)
        ingredient_3 = Ingredient('peanuts', IngredientType.NUTS)
        ingredient_4 = Ingredient('bread', IngredientType.GRAIN)
        ingredient_5 = Ingredient('pinto beans', IngredientType.BEANS)
        ingredient_6 = Ingredient('steak', IngredientType.MEAT)
        ingredient_7 = Ingredient('salmon', IngredientType.FISH)
        ingredient_8 = Ingredient('milk', IngredientType.DAIRY)
        ingredient_9 = Ingredient('oregano', IngredientType.SEASONING)

        self.assertEqual(ingredient_1.getIngredientType(), IngredientType.VEGETABLE.name)
        self.assertEqual(ingredient_2.getIngredientType(), IngredientType.FRUIT.name)
        self.assertEqual(ingredient_3.getIngredientType(), IngredientType.NUTS.name)
        self.assertEqual(ingredient_4.getIngredientType(), IngredientType.GRAIN.name)
        self.assertEqual(ingredient_5.getIngredientType(), IngredientType.BEANS.name)
        self.assertEqual(ingredient_6.getIngredientType(), IngredientType.MEAT.name)
        self.assertEqual(ingredient_7.getIngredientType(), IngredientType.FISH.name)
        self.assertEqual(ingredient_8.getIngredientType(), IngredientType.DAIRY.name)
        self.assertEqual(ingredient_9.getIngredientType(), IngredientType.SEASONING.name)        


if __name__ == '__main__':
    unittest.main()

    
