import pytest
from nutritional_calculator import fetch_nutritional_data, calculate_total_nutrition
from pytest import approx

def test_fetch_nutritional_data(tmp_path):
    # Create a temporary CSV file with extended nutritional data
    data = """food_item,calories,protein,fat,carbs
apple,52,0.3,0.2,14
banana,89,1.1,0.3,23
bread,265,9,3.2,49
chicken_breast,165,31,3.6,0
rice,130,2.7,0.3,28
broccoli,55,3.7,0.6,11
almonds,579,21,49,22
milk,42,3.4,1,5
egg,155,13,11,1.1
salmon,208,20,13,0
potato,77,2,0.1,17
carrot,41,0.9,0.2,10
spinach,23,2.9,0.4,3.6
yogurt,59,10,0.4,3.6
cheese,402,25,33,1.3
orange,47,0.9,0.1,12
beef,250,26,15,0
pasta,131,5,1.1,25
beans,347,21,1.2,63
avocado,160,2,15,9
bacon,30,12,6.2,8
pineapple,42,2.1,1.1,18
"""
    file = tmp_path / "nutritional_data.csv"
    file.write_text(data)

    # Test fetching nutritional data
    data = fetch_nutritional_data("apple", file)
    assert data == {"calories": 52, "protein": 0.3, "fat": 0.2, "carbs": 14}

    data = fetch_nutritional_data("banana", file)
    assert data == {"calories": 89, "protein": 1.1, "fat": 0.3, "carbs": 23}

    data = fetch_nutritional_data("chicken_breast", file)
    assert data == {"calories": 165, "protein": 31, "fat": 3.6, "carbs": 0}

    data = fetch_nutritional_data("unknown", file)
    assert data == {}

def test_calculate_total_nutrition(tmp_path):
    # Create a temporary CSV file with extended nutritional data
    data = """food_item,calories,protein,fat,carbs
apple,52,0.3,0.2,14
banana,89,1.1,0.3,23
bread,265,9,3.2,49
chicken_breast,165,31,3.6,0
rice,130,2.7,0.3,28
broccoli,55,3.7,0.6,11
almonds,579,21,49,22
milk,42,3.4,1,5
egg,155,13,11,1.1
salmon,208,20,13,0
potato,77,2,0.1,17
carrot,41,0.9,0.2,10
spinach,23,2.9,0.4,3.6
yogurt,59,10,0.4,3.6
cheese,402,25,33,1.3
orange,47,0.9,0.1,12
beef,250,26,15,0
pasta,131,5,1.1,25
beans,347,21,1.2,63
avocado,160,2,15,9
bacon,30,12,6.2,8
pineapple,42,2.1,1.1,18
"""
    file = tmp_path / "nutritional_data.csv"
    file.write_text(data)

    # Test calculating total nutrition
    food_items = {"apple": 200, "banana": 100, "chicken_breast": 150}
    result = calculate_total_nutrition(food_items, file)
    expected = {
        "calories": 52 * 2 + 89 * 1 + 165 * 1.5,
        "protein": 0.3 * 2 + 1.1 * 1 + 31 * 1.5,
        "fat": 0.2 * 2 + 0.3 * 1 + 3.6 * 1.5,
        "carbs": 14 * 2 + 23 * 1 + 0 * 1.5,
    }
    assert result["calories"] == approx(expected["calories"])
    assert result["protein"] == approx(expected["protein"])
    assert result["fat"] == approx(expected["fat"])
    assert result["carbs"] == approx(expected["carbs"])

# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])
