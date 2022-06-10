# 2115. Find All Possible Recipes from Given Supplies

# Solution 1: My approach 97.7% faster
# We start processing each recipe one by one
# Wherever we encounter an ingredient in the recipe ingredients which is also a recipe,
# we start processing it first and we go like this recursively
# We also use memoization to store the results of each intermediate ingredient/recipe calculated
class Solution:
    def isPossible(self, receipe_ingredient_map, ingre_curr, recipe_curr):
        for ingre in ingre_curr:
            # ingredient is not another recipe
            if ingre not in receipe_ingredient_map:
                if ingre in self.supplies:
                    continue
                else:
                    return False
            
            # ingredient is another recipe
            else:
                # this ingredient has been processed before
                if ingre in self.recipe_possible:
                    # if this recipe is not possible, parent recipe is
                    # not possible as well, so we directly return False
                    if not self.recipe_possible[ingre]:
                        return False
                    
                    # if this recipe is possible we continue to checking
                    # other ingredients
                    else:
                        continue
                
                # cyclic loop exists - we need the recipe as an ingredient for the recipe
                if ingre in recipe_curr:
                    return False
                
                # the curr ingre is also a recipe, so process it first
                else:                    
                    recipe_curr.add(ingre)
                    self.recipe_possible[ingre] = self.isPossible(receipe_ingredient_map, receipe_ingredient_map[ingre], recipe_curr)
                    
                    if not self.recipe_possible[ingre]:
                        return False
        # if all ingredients have been processed for a recipe
        # and we didn't return False, then this recipe is possible
        return True
    
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        receipe_ingredient_map = dict()
        final_list = list()
        self.supplies = set(supplies)
        
        # memoization of already checked recipes
        self.recipe_possible = dict()
        
        for i in range(len(recipes)):
            receipe_ingredient_map[recipes[i]] = ingredients[i]
        
        for recipe, ingre_curr in receipe_ingredient_map.items():
            if recipe in self.recipe_possible:
                continue
            
            # keep a track of the recipes so that if a cyclic loop
            # of recipes exist we can detect it
            recipe_curr = set()
            recipe_curr.add(recipe)
            
            self.recipe_possible[recipe] = self.isPossible(receipe_ingredient_map, ingre_curr, recipe_curr)
            
        for recipe, possible in self.recipe_possible.items():
            if possible:
                final_list.append(recipe)
        
        return final_list

# Solution 2: Using graph and topological sort
from collections import defaultdict

class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        ingredient_recipe_map = defaultdict(list)
        ans = list()

        for i in range(len(recipes)):
            for ingredient in ingredients[i]:
                ingredient_recipe_map[ingredient].append(recipes[i])

        indeg = {recipes[i]: len(ingredients[i]) for i in range(len(recipes))}

        q = list()
        q.extend(supplies)

        while q:
            supply = q.pop()

            if supply in ingredient_recipe_map:
                for recipe in ingredient_recipe_map[supply]:
                    indeg[recipe] -= 1

                    if indeg[recipe] == 0:
                        q.append(recipe)
                        ans.append(recipe)

        return ans