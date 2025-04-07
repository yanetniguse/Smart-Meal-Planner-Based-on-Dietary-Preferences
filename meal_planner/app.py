from flask import Flask, render_template, request
from meal_rules import MealPlanner, UserPreferences

app = Flask(__name__)

# Sample meals database
meals = [
    {"name": "Grilled Chicken", "diet": "non-vegetarian", "tags": ["high protein", "low carb"]},
    {"name": "Chickpea Salad", "diet": "vegetarian", "tags": ["high protein", "gluten-free"]},
    {"name": "Tofu Stir-fry", "diet": "vegetarian", "tags": ["low carb", "high protein"]},
    {"name": "Quinoa Salad", "diet": "vegetarian", "tags": ["low carb", "gluten-free"]},
    {"name": "Beef Steak", "diet": "non-vegetarian", "tags": ["high protein"]},
    {"name": "Vegetable Curry", "diet": "vegetarian", "tags": ["gluten-free"]},
]

# Rule-based meal suggestion logic
def suggest_meals(user_diet, preferences):
    suggestions = []
    for meal in meals:
        if meal["diet"] == user_diet and all(pref in meal["tags"] for pref in preferences):
            suggestions.append(meal["name"])
    return suggestions

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        diet = request.form['diet']
        preferences = request.form.getlist('preferences')

        engine = MealPlanner()
        engine.reset()
        engine.declare(UserPreferences(diet=diet, preferences=preferences))
        engine.run()

        return render_template('result.html', meals=engine.suggestions)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
