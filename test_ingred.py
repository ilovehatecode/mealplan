##Unit Testing
import unittest
##Import module to test
from ingredient import Ingredient, IngredientType

class TestIngredient(unittest.TestCase):

    def setUp(self):
        self.ingredient_1 = Ingredient('green pepper', IngredientType.VEGETABLE)
        self.ingredient_2 = Ingredient('green apple', IngredientType.FRUIT)
        self.ingredient_3 = Ingredient('peanuts', IngredientType.NUTS)
        self.ingredient_4 = Ingredient('bread', IngredientType.GRAIN)
        self.ingredient_5 = Ingredient('pinto beans', IngredientType.BEANS)
        self.ingredient_6 = Ingredient('steak', IngredientType.MEAT)
        self.ingredient_7 = Ingredient('salmon', IngredientType.FISH)
        self.ingredient_8 = Ingredient('milk', IngredientType.DAIRY)
        self.ingredient_9 = Ingredient('oregano', IngredientType.SEASONING)

    def tearDown(self):
        pass
    
    def test_ingredientname(self):
        self.assertEqual(self.ingredient_1.getIngredientName(), 'GREEN PEPPER')
        self.assertEqual(self.ingredient_2.getIngredientName(), 'GREEN APPLE')
        self.assertEqual(self.ingredient_3.getIngredientName(), 'PEANUTS')
        self.assertEqual(self.ingredient_4.getIngredientName(), 'BREAD')
        self.assertEqual(self.ingredient_5.getIngredientName(), 'PINTO BEANS')
        self.assertEqual(self.ingredient_6.getIngredientName(), 'STEAK')
        self.assertEqual(self.ingredient_7.getIngredientName(), 'SALMON')
        self.assertEqual(self.ingredient_8.getIngredientName(), 'MILK')
        self.assertEqual(self.ingredient_9.getIngredientName(), 'OREGANO')

    def test_ingredienttype(self):
        self.assertEqual(self.ingredient_1.getIngredientType(), IngredientType.VEGETABLE.name)
        self.assertEqual(self.ingredient_2.getIngredientType(), IngredientType.FRUIT.name)
        self.assertEqual(self.ingredient_3.getIngredientType(), IngredientType.NUTS.name)
        self.assertEqual(self.ingredient_4.getIngredientType(), IngredientType.GRAIN.name)
        self.assertEqual(self.ingredient_5.getIngredientType(), IngredientType.BEANS.name)
        self.assertEqual(self.ingredient_6.getIngredientType(), IngredientType.MEAT.name)
        self.assertEqual(self.ingredient_7.getIngredientType(), IngredientType.FISH.name)
        self.assertEqual(self.ingredient_8.getIngredientType(), IngredientType.DAIRY.name)
        self.assertEqual(self.ingredient_9.getIngredientType(), IngredientType.SEASONING.name)        


if __name__ == '__main__':
    unittest.main()

    
