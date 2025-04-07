from experta import *

class UserPreferences(Fact):
    """User dietary preferences"""
    pass

class MealPlanner(KnowledgeEngine):
    def __init__(self):
        super().__init__()
        self.suggestions = []

    @Rule(UserPreferences(diet='vegetarian', preferences=MATCH.prefs))
    def veg_meals(self, prefs):
        if 'high protein' in prefs:
            self.suggestions.append('Tofu Stir-fry')
            self.suggestions.append('Chickpea Salad')
        if 'low carb' in prefs:
            self.suggestions.append('Quinoa Salad')
        if 'gluten-free' in prefs:
            self.suggestions.append('Vegetable Curry')

    @Rule(UserPreferences(diet='non-vegetarian', preferences=MATCH.prefs))
    def non_veg_meals(self, prefs):
        if 'high protein' in prefs:
            self.suggestions.append('Grilled Chicken')
            self.suggestions.append('Beef Steak')
        if 'low carb' in prefs:
            self.suggestions.append('Grilled Chicken')
        if 'gluten-free' in prefs:
            self.suggestions.append('Grilled Chicken')
