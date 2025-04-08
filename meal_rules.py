from experta import *

class UserPreferences(Fact):
    """User dietary preferences"""
    pass

class MealPlanner(KnowledgeEngine):
    def __init__(self):
        super().__init__()
        self.suggestions = {"breakfast": [], "lunch": [], "dinner": []}

    @Rule(UserPreferences(diet='vegetarian', preferences=MATCH.prefs))
    def veg_meals(self, prefs):
        # Breakfast suggestions
        if 'low carb' in prefs or 'high protein' in prefs:
            self.suggestions["breakfast"].append("Oatmeal with Fruits")
            self.suggestions["breakfast"].append("Smoothie with Almond Milk")
        if 'gluten-free' in prefs:
            self.suggestions["breakfast"].append("Avocado Toast with Tomatoes")

        # Lunch suggestions
        if 'high protein' in prefs:
            self.suggestions["lunch"].append("Tofu Stir-fry")
            self.suggestions["lunch"].append("Chickpea Salad")
        if 'low carb' in prefs:
            self.suggestions["lunch"].append("Quinoa Salad")
        if 'gluten-free' in prefs:
            self.suggestions["lunch"].append("Vegetable Curry")

        # Dinner suggestions
        if 'high protein' in prefs or 'low carb' in prefs:
            self.suggestions["dinner"].append("Tofu Stir-fry")
        if 'gluten-free' in prefs:
            self.suggestions["dinner"].append("Vegetable Curry")

    @Rule(UserPreferences(diet='non-vegetarian', preferences=MATCH.prefs))
    def non_veg_meals(self, prefs):
        # Breakfast suggestions
        if 'high protein' in prefs or 'low carb' in prefs:
            self.suggestions["breakfast"].append("Scrambled Eggs with Spinach")
            self.suggestions["breakfast"].append("Greek Yogurt with Nuts")
        if 'gluten-free' in prefs:
            self.suggestions["breakfast"].append("Boiled Eggs with Avocado")

        # Lunch suggestions
        if 'high protein' in prefs:
            self.suggestions["lunch"].append("Grilled Chicken")
            self.suggestions["lunch"].append("Beef Steak")
        if 'low carb' in prefs:
            self.suggestions["lunch"].append("Grilled Chicken Salad")
        if 'gluten-free' in prefs:
            self.suggestions["lunch"].append("Chicken Lettuce Wraps")

        # Dinner suggestions
        if 'high protein' in prefs:
            self.suggestions["dinner"].append("Beef Steak")
            self.suggestions["dinner"].append("Grilled Chicken")
        if 'low carb' in prefs:
            self.suggestions["dinner"].append("Grilled Chicken")
        if 'gluten-free' in prefs:
            self.suggestions["dinner"].append("Grilled Chicken")
