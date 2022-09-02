import streamlit
import pandas as pd
import requests

streamlit.title('My parents first healthy Diner')

streamlit.header('Breakfast Menu')
streamlit.text('Omega 3 Blueberry Oatmeal')
streamlit.text('Kale, Spinach & Rocket Smoothie')
streamlit.text('Hard-Boiled Free-Range Egg')

my_fruit_list = pd.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

my_fruit_list.set_index('Fruit', inplace=True)

# Let's put a pick list here so they can pick the fruit they want to include 
fruit_selected= streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])

fruit_to_show = my_fruit_list.loc[fruit_selected]


streamlit.dataframe(fruit_to_show)

streamlit.header("Fruityvice Fruit Advice!")


fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
streamlit.text(fruityvice_response.json())


fruityvice_normalized = pd.json_normalize(fruityvice_response.json())

streamlit.dataframe(fruityvice_normalized)
