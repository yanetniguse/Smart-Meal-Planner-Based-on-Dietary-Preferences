# SMART-MEAL-PLANNER (based on dietry preferences)
- `Objective:` Suggest meal plans based on user preferences
- `Technologies:` Python, Rule-Based system, Flask
- `Methodologies:` Knowledge representation using IF-THEN rules

## Overview
The Smart Meal Planner is a simple web application designed to help users create personalized meal plans based on their dietary preferences and restrictions. Built using Python and Flask, this version of the app is a simplified, locally run system that suggests meal options based on a set of predefined rules.

## Features
- `User Input:` Users can input their dietary preferences (e.g., vegetarian, gluten-free, low-carb).
- `Personalized Meal Suggestions:` Based on the user input, the app generates a simple meal plan with suggestions for breakfast, lunch, and dinner.
- `Rule-Based System:` The app uses the experta rule engine to evaluate user preferences and generate meal recommendations.

## Technologies Used
- `Python:` The main programming language for the app.
- `Flask:` A lightweight Python web framework used to create the web application and serve the user interface.
- `experta:`A rule-based engine that processes user inputs and provides meal suggestions.
- `HTML:` Basic HTML for rendering the user interface.

## Installation
To set up the Smart Meal Planner locally:
1. Clone the Repository
   ``` bash
   git clone https://github.com/your-username/smart-meal-planner.git
   cd smart-meal-planner ```
2. Create a Virtual Environment
   ``` bash
   python -m venv venv
   source venv/bin/activate ```
3. Install the Dependencies
   ``` bash
   pip install -r requirements.txt ```
4. Run the Application
   ``` python
   python app.py ```
The app will be available at http://127.0.0.1:5000.

## Usage
- `Open the Home Page:` Navigate to http://127.0.0.1:5000 in your browser.
- `Enter Your Preferences:` Provide dietary preferences like vegetarian or gluten-free.
- `Generate Meal Plan:` Click "Generate Meal Plan" to see meal suggestions based on your preferences.


## File Breakdown
### `app.py` - Flask app
Handles:
- User form submission
- Passing input to rule engine
- Returning meal suggestions to the result page

### `meal_rules.py` - Rule Engine(experta)
Defines:
- User preferences as a Fact
- Rule-based logic to suggest meals

### templates/
The `templates` directory contains the HTML files used by Flask to render pages.
- `index.html:` Contains the user input form
- `result.html:` Contains the output page for suggested meals

## Contributing
1. Fork the repository.
2. Create a new branch
3. Commit your changes
4. Push to the branch
5. Create a new Pull Request.

## Authors
- [James Mang'ana] - @jayotieno
- [Yanet Niguse] - @yanetniguse
- [Dhruv Pokhariyal] - @POlcahontas
- [Kwame Lucheveli] - @luche3002

## Instructor
Prof. Austin Odera