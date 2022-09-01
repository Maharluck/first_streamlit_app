import streamlit
import pandas as pd


streamlit.title('My parents first healthy Diner')

streamlit.header('Breakfast Menu')
streamlit.text('Omega 3 Blueberry Oatmeal')
streamlit.text('Kale, Spinach & Rocket Smoothie')
streamlit.text('Hard-Boiled Free-Range Egg')

my_fruit_list = pd.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")



# Let's put a pick list here so they can pick the fruit they want to include 
streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))

my_fruit_list.set_index('Fruit')


streamlit.dataframe(my_fruit_list)

