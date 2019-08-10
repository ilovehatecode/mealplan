
class Dish:

        def __init__(self, ingredients, recipe):
                if type(ingredients) != list:
                        raise 'Ingredients must be a list'
                else:   
                    self.ingredients = ingredients
                    
                if type(recipe) != str:
                        raise 'recipe must be  string'
                else:
                        self.recipe = recipe


        def getIngredients(self):
                return self.ingredients

        def getRecipe(self):
                return self.recipe

        



        

        
        
