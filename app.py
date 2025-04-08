from flask import Flask, render_template, request
from meal_rules import MealPlanner, UserPreferences
from experta import *

app = Flask(__name__)

# Meals database with breakfast, lunch, and dinner categories
meals = [
        {"name": "Grilled Chicken", "diet": "non-vegetarian", "tags": ["high protein", "low carb"], "meal_type": "lunch"},
        {"name": "Chickpea Salad", "diet": "vegetarian", "tags": ["high protein", "gluten-free"], "meal_type": "lunch"},
        {"name": "Tofu Stir-fry", "diet": "vegetarian", "tags": ["low carb", "high protein"], "meal_type": "lunch"},
        {"name": "Quinoa Salad", "diet": "vegetarian", "tags": ["low carb", "gluten-free"], "meal_type": "lunch"},
        {"name": "Beef Steak", "diet": "non-vegetarian", "tags": ["high protein"], "meal_type": "dinner"},
        {"name": "Vegetable Curry", "diet": "vegetarian", "tags": ["gluten-free"], "meal_type": "dinner"},
        {"name": "Scrambled Eggs with Spinach", "diet": "non-vegetarian", "tags": ["low carb", "high protein"], "meal_type": "breakfast"},
        {"name": "Oatmeal with Fruits", "diet": "vegetarian", "tags": ["gluten-free", "low carb"], "meal_type": "breakfast"},
        {"name": "Smoothie with Almond Milk", "diet": "vegetarian", "tags": ["gluten-free", "low carb"], "meal_type": "breakfast"},
        {"name": "Avocado Toast with Tomatoes", "diet": "vegetarian", "tags": ["gluten-free", "low carb"], "meal_type": "breakfast"},
    ]

# Rule-based meal suggestion logic
def suggest_meals(user_diet, preferences, meal_type):
    suggestions = []
    for meal in meals:
        if meal["diet"] == user_diet and all(pref in meal["tags"] for pref in preferences) and meal["meal_type"] == meal_type:
            suggestions.append(meal["name"])
    return suggestions

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        diet = request.form['diet']
        preferences = request.form.getlist('preferences')  # Collect preferences as a list

        engine = MealPlanner()
        engine.reset()
        engine.declare(UserPreferences(diet=diet, preferences=preferences))  # Declare preferences as a fact
        engine.run()

        # If no suggestions, display a message
        if not engine.suggestions["breakfast"] and not engine.suggestions["lunch"] and not engine.suggestions["dinner"]:
            return render_template('index.html', message="No meals found matching your preferences.")

        # Get meal suggestions for breakfast, lunch, and dinner
        breakfast_suggestions = engine.suggestions["breakfast"]
        lunch_suggestions = engine.suggestions["lunch"]
        dinner_suggestions = engine.suggestions["dinner"]

        return render_template('result.html',
                       breakfast=engine.suggestions["breakfast"],
                       lunch=engine.suggestions["lunch"],
                       dinner=engine.suggestions["dinner"])

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
