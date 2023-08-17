import streamlit as st

# Mock recipes database
RECIPES = {
    "Pasta Aglio e Olio": {"ingredients": ["pasta", "garlic", "olive oil", "red pepper flakes", "parsley"]},
    "Peanut Butter & Jelly Sandwich": {"ingredients": ["bread", "peanut butter", "jelly"]},
    "Scrambled Eggs": {"ingredients": ["eggs", "butter", "salt", "pepper"]},
    "Mashed Potatoes": {"ingredients": ["potatoes", "butter", "milk", "salt"]},
}

def find_recipes(ingredients_list):
    """Find recipes based on ingredients."""
    matching_recipes = []
    for recipe_name, recipe_info in RECIPES.items():
        if all(ingredient in ingredients_list for ingredient in recipe_info["ingredients"]):
            matching_recipes.append(recipe_name)
    return matching_recipes

# Streamlit app
st.title("Recipe Suggester")

# User input
ingredients_input = st.text_area("Enter ingredients you have (comma separated):")
ingredients_list = [ingredient.strip().lower() for ingredient in ingredients_input.split(",")]

if st.button("Find Recipes"):
    if ingredients_input:
        suggested_recipes = find_recipes(ingredients_list)
        if suggested_recipes:
            st.write("Here are some recipes you can make:")
            for recipe in suggested_recipes:
                st.write(f"- {recipe}")
        else:
            st.write("Sorry, no matching recipes found for the given ingredients. Try adding more ingredients.")
    else:
        st.write("Please enter some ingredients.")
