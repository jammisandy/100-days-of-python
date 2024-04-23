import requests
from datetime import datetime

GENDER = "Male"
HEIGHT = "165"
WEIGHT = "90"
AGE = "35"

APP_ID = "dffea7cd"
API_KEY = "b249d4e8cfba497b6ceee6fb5252761a"

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheet_endpoint = "https://api.sheety.co/0d5a7a26b507fcb0304233c6f96f791d/myWorkouts/workouts"

exercise_text = input("Tell me which exercise you did: ")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY
}

parameters = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT,
    "height_cm": HEIGHT,
    "age": AGE
}

response = requests.post(exercise_endpoint, json=parameters, headers=headers)
result = response.json()
##print(result)

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    sheet_response = requests.post("https://api.sheety.co/0d5a7a26b507fcb0304233c6f96f791d/myWorkouts/workouts", json=sheet_inputs)
    ##sheet_response = requests.post(sheet_endpoint,json=sheet_inputs,auth=("username":sandy9493,"password":Admin@123456))

    print(sheet_response.text)