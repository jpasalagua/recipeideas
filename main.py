import streamlit as st
import openai

# Initialize OpenAI GPT-3 client
openai.api_key = 'YOUR_OPENAI_API_KEY'

def gpt3_recipe_suggestion(ingredients):
    """Get recipe suggestion from GPT-3 based on ingredients."""
    prompt_text = f"I have the following ingredients: {', '.join(ingredients)}. What's a simple recipe I can make with them?"
    response = openai.Completion.create(engine="davinci", prompt=prompt_text, max_tokens=150)
    return response.choices[0].text.strip()

# Streamlit app
st.title("GPT-3 Recipe Suggester")

# User input
ingredients_input = st.text_area("Enter ingredients you have (comma separated):")
ingredients_list = [ingredient.strip().lower() for ingredient in ingredients_input.split(",")]

if st.button("Find Recipes"):
    if ingredients_input:
        suggested_recipe = gpt3_recipe_suggestion(ingredients_list)
        st.write("Here's a recipe suggestion from GPT-3:")
        st.write(suggested_recipe)
    else:
        st.write("Please enter some ingredients.")
