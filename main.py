import requests
import smtplib
import os

# GET the food cooking instruction.

API_ENDPOINT = "https://www.themealdb.com/api/json/v1/1/search.php"

food_name = input("What food would you like to get the recipe of?: ")

food_params = {
  "s": food_name
}

recipe_response = requests.get(url=API_ENDPOINT, params=food_params)
recipe_data = recipe_response.json()

meal_name = recipe_data["meals"][0]["strMeal"]
meal_instructions = recipe_data["meals"][0]["strInstructions"]

# Email Credentials

EMAIL = os.environ["EMAIL"]
PASSWORD = os.environ["PASSWORD"]
TO_EMAIL = os.environ["TO_EMAIL"]

with smtplib.SMTP("smtp.gmail.com") as connection:
  connection.starttls()
  connection.login(user=EMAIL, password=PASSWORD)
  connection.sendmail(
    from_addr=EMAIL, 
    to_addrs="ash61626@gmail.com", 
    msg=f"Subject:How to make some {meal_name}!\n\nHere's some instructions to making {meal_name}!\n\n{meal_instructions}".encode('utf-8')
  )
  