import csv
import argparse

def get_user_input(nutritional_data_file):
    """Collect user input for food items and quantities."""
    food_items = {}
    print("Enter food items and quantities (type 'done' to finish):")
    
    known_items = set()
    with open(nutritional_data_file, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            known_items.add(row['food_item'].lower())

    while True:
        item = input("Food item: ").strip().lower()
        if item == 'done':
            break
        if item not in known_items:
            print("Food item not found in the nutritional data. Please try again.")
            continue
        try:
            quantity = float(input("Quantity (grams): "))
        except ValueError:
            print("Invalid quantity. Please enter a number.")
            continue
        food_items[item] = food_items.get(item, 0) + quantity
    return food_items

def fetch_nutritional_data(food_item, nutritional_data_file):
    """Retrieve nutritional data for a given food item from a CSV file."""
    with open(nutritional_data_file, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row['food_item'].lower() == food_item:
                return {
                    "calories": float(row["calories"]),
                    "protein": float(row["protein"]),
                    "fat": float(row["fat"]),
                    "carbs": float(row["carbs"]),
                }
    return {}

def calculate_total_nutrition(food_items, nutritional_data_file):
    """Calculate the total nutritional values based on input."""
    total_nutrition = {"calories": 0, "protein": 0, "fat": 0, "carbs": 0}
    for item, quantity in food_items.items():
        nutrition = fetch_nutritional_data(item, nutritional_data_file)
        if nutrition:
            total_nutrition["calories"] += nutrition["calories"] * (quantity / 100)
            total_nutrition["protein"] += nutrition["protein"] * (quantity / 100)
            total_nutrition["fat"] += nutrition["fat"] * (quantity / 100)
            total_nutrition["carbs"] += nutrition["carbs"] * (quantity / 100)
    return total_nutrition

def display_nutritional_info(total_nutrition):
    """Display the calculated nutritional information."""
    print("\nTotal Nutritional Information:")
    print(f"Calories: {total_nutrition['calories']:.2f} kcal")
    print(f"Protein: {total_nutrition['protein']:.2f} g")
    print(f"Fat: {total_nutrition['fat']:.2f} g")
    print(f"Carbohydrates: {total_nutrition['carbs']:.2f} g")

def main():
    parser = argparse.ArgumentParser(description='Nutritional Information Calculator')
    parser.add_argument('nutritional_data_file', nargs='?', default='nutritional_data.csv',
                        help='Path to the nutritional data CSV file (default: nutritional_data.csv)')
    args = parser.parse_args()

    food_items = get_user_input(args.nutritional_data_file)
    total_nutrition = calculate_total_nutrition(food_items, args.nutritional_data_file)
    display_nutritional_info(total_nutrition)

if __name__ == "__main__":
    main()
