# Nutritional Information Calculator 

## Overview:

The Nutritional Information Calculator is a Python program that allows users to manage and analyze nutritional data for various food items. Users can add new food items to a CSV file, then calculate the total nutritional intake based on the quantities of foods they consume. The program is designed to be flexible, enabling users to easily update the nutritional database and obtain detailed nutritional information.

## Features: 

Add Food Items: Users can add new food items along with their nutritional values (calories, protein, fat, carbs) to the CSV file.
Calculate Nutrition: Users can input the food items and their quantities to calculate the total nutritional intake.
Menu-Driven Interface: The program offers a simple, interactive menu for easy navigation.

## Installation:

Clone the Repository:
git clone https://github.com/Patfarmurs/nutritional_calculator.git
cd nutritional_calculator
Ensure Python is Installed:
The program requires Python 3.6 or higher. You can check your Python version by running:
python --version

## Install Required Modules:

There are no external modules required, as the program relies on standard Python libraries.

## Usage

Running the Program:
To run the program, use the following command:

python nutritional_calculator.py
By default, the program uses nutritional_data.csv as the database file. If you want to use a different CSV file, specify the file name as an argument:

python nutritional_calculator.py path/to/your/nutritional_data.csv
Program Options
Upon running the program, you will be presented with a menu:

Add a New Food Item: Allows you to add new food items to the CSV file. You will be prompted to enter the food item's name, along with its nutritional values per 100 grams (calories, protein, fat, carbs).

Calculate Total Nutrition: Prompts you to input the food items and quantities consumed. The program then calculates and displays the total nutritional values based on the data in the CSV file.

## Exit: Closes the program.

** Example

Here's how you might interact with the program:
Choose an option:
1. Add a new food item
2. Calculate total nutrition
3. Exit
Enter your choice: 1

Add a new food item:
Food item: orange
Calories per 100g: 47
Protein per 100g (g): 0.9
Fat per 100g (g): 0.1
Carbohydrates per 100g (g): 12
Food item 'orange' added successfully.

Choose an option:
1. Add a new food item
2. Calculate total nutrition
3. Exit
Enter your choice: 2

Enter food items and quantities (type 'done' to finish):
Food item: orange
Quantity (grams): 150
Food item: done

Total Nutritional Information:
Calories: 70.50 kcal
Protein: 1.35 g
Fat: 0.15 g
Carbohydrates: 18.00 g
CSV File Format
The CSV file should contain the following columns:

food_item: The name of the food item (e.g., "apple").
calories: The number of calories per 100 grams.
protein: The amount of protein per 100 grams (in grams).
fat: The amount of fat per 100 grams (in grams).
carbs: The amount of carbohydrates per 100 grams (in grams).

** Example CSV Content: 

food_item,calories,protein,fat,carbs
apple,52,0.3,0.2,14
banana,89,1.1,0.3,23
bread,265,9,3.2,49
orange,47,0.9,0.1,12
Assumptions
The CSV file is well-formatted and contains valid data.
All nutritional values are based on 100 grams of the food item.
The user will input food items that are present in the CSV file.
Contribution
If you'd like to contribute to this project, feel free to fork the repository, make your changes, and submit a pull request. Contributions are always welcome!

## License
This project is licensed under the MIT License - <a href="LICENSE">MIT</a>.
