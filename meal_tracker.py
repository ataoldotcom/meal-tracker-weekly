## running the v1 meal planner template

#importing libraries
from jinja2 import Environment, FileSystemLoader


#set the environment
env = Environment(loader = FileSystemLoader('templates'))

#load the template
try:
    template = env.get_template('meal_tracker.jinja')
    print("Template loaded successfully")
except Exception as e:
    print(f"Error! Template could not be loaded: {e}")

#data User needs to update this meals. 
try:
    meal_data = {
        "calorie_goal": 2500,
        "customer_name": "Blanche",
        "month_dates": "Nov 25-26th,",
        "meals_by_day": {
            "Monday": {
                "breakfast": [
                    {"meal": "Egg-white Breakfast cups", "calories": 170, "is_high_protein": True},
                    {"meal": "Greek Yogurt with Berries", "calories": 100, "is_high_protein": True}
                ],
                "lunch": [
                    {"meal": "Grilled Chicken Salad", "calories": 300, "is_high_protein": True},
                    {"meal": "Quinoa and Veggie Bowl", "calories": 250, "is_high_protein": False}
                ],
                "dinner": [
                    {"meal": "Salmon", "calories": 400, "is_high_protein": True},
                    {"meal": "Roated Veggies", "calories": 300, "is_high_protein": False}
                ],
            },
            "Tuesday": { #if more days are needed COPY the structure of the dictionary starting from this ENTIRE LINE including indentation
                "breakfast": [
                    {"meal": "Egg-white Breakfast cups", "calories": 170, "is_high_protein": True},
                    {"meal": "Protein Smoothie", "calories": 150, "is_high_protein": True}
                ],
                "lunch": [
                    {"meal": "Grilled Steak bowl", "calories": 600, "is_high_protein": True},
                    {"meal": "Spinach Breakfast Salad", "calories": 160, "is_high_protein": False}
                ],
                "dinner": [
                    {"meal": "Stir Fry", "calories": 420, "is_high_protein": False},
                    {"meal": "White Rice", "calories": 220, "is_high_protein": False}
                ],
            },#Include this trailing semicolon!
# <---PASTE on this line BEFORE the #. Multiple days can be added as needed. Update the correct day name
        }
    }
            
    print("Data parsed in template.\n\n")
except Exception as ex:
    print(f"Error! Data could not be parsed in template: {ex}")

#calculation for daily calorie counter
for day, meals in meal_data["meals_by_day"].items():
    total_calories = 0
    for meal_type, meal_list in meals.items():
        if isinstance(meal_list, list):
            total_calories += sum(meal["calories"] for meal in meal_list)
    meals["total_calories"] = total_calories

#calculation of weekly calories  
weekly_total_calories = sum(meals["total_calories"] for meals in meal_data["meals_by_day"].values())

#calculation of weekly calorie goal
number_of_days = len(meal_data["meals_by_day"])
weekly_calorie_goal = number_of_days * meal_data["calorie_goal"]

#debug which variable isn't an int:
#print("Type of weekly_total_calories:", type(weekly_total_calories))
#print("Type of weekly_calorie_goal:", type(weekly_calorie_goal))
#print("Type of meal_data['calorie_goal']:", type(meal_data["calorie_goal"]))
#print("Type of number_of_days:", type(number_of_days))

#render data in template format
try:
    meal_tracker = template.render(meal_data=meal_data, weekly_total_calories=weekly_total_calories, weekly_calorie_goal=weekly_calorie_goal)
    print(meal_tracker)
except Exception as exc:
    print(f"Error! Meal planner could not be printed: {exc}")
