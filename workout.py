# run me in your terminal
# by typing python3.10 workout.py
# and pressing enter

import random

# Ask user for name, strip whitespace, capitalize 
name = input("Please enter your name: ").strip().title()

def welcome():
  print(f"Hi, {name}! Welcome to your personalized fitness App." " " "(◕‿◕✿)")
  print("--------")
  print("Please follow the instructions to get started")


def instructions():
  print("Instructions: You'll do 4 sets / 12 reps per exercise.")
  print("Please take a 40 second rest between sets.")
  print("--------")
  print("Make sure to warm up before starting.")
  print("--------")

def start_up():
  print("What would you like to workout today?")
  print("Lower Body")
  print("Upper Body")
  print("Core")
  print("Cardio")


welcome()
instructions()
start_up()

# Excercise variables

lower_body = ['Quads', 'Hamstrings', 'Glutes']

upper_body = ['Back & Biceps', 'Shoulders & Triceps']

leg_ex = {

    'quads_1': ["Barbell Squats", "Lunges", "Pigeon Lunges", "Sumo Leg Press", "Narrow Leg Press", "Leg Extensions", "Bulgarian Split Squats"],
    'hamstrings_1': ["Romanian Deadlifts", "Sumo Deadlifts", "Lying Leg Curl", "Swiss-Ball Leg Curl", "Hip-Thrusts", "Stiff Leg Deadlifts", "Single-Leg Deadlifts"],
    'glutes_1': ['Barbell Hip-Thrusts', 'Bulgarian Split Squats', 'Frog Pump', 'Cable Kickbacks', 'Banded Hip-Thrusts', 'Banded Frog Kicks', 'Single-leg Hip-Thrusts']
}

upper_ex = {
    'b_b': ['Lat Pulldowns', "Assited Push Ups", "Barbell Bicep Curls", "Trx Inverted Rows" "Seated Rows", "Bent-Over Rows", "Assisted Pull-Ups", "T-Bar Rows", "Single-Arm Dumbbell Row"],

    's_t': ['Shoulder Taps', 'Seated Arnold Press', 'Dumbbell Chest Press','Seated Front Raises', 'Dumbbell Lateral Raises', 'Cable Single Arm Pull Downs', 'Push Ups', 'Cable Tricep Pushdowns']
}

cardio = ("Steady State Bike", "Elliptical Sprints", "Med Ball Slams", 'Box Jumps', "Steady Skate Bike")

core = ("30 sec Plank", "Leg Raises", "30 sec Oblique planks", "Anchored Russian Twists", "Toe Taps", 'Mountain Climbers')  

terminate = False

while not terminate:
    print("--------")

    user_input = input('> ') 

    if user_input == "quit":
      terminate = True

    if user_input == "Lower Body".casefold():
      print(lower_body)  

    elif user_input == "Quads".casefold():
      print(random.sample(leg_ex['quads_1'], 4))

    elif user_input == "Hamstrings".casefold():
      print(random.sample(leg_ex['hamstrings_1'], 4))  

    elif user_input == "Glutes".casefold():
      print(random.sample(leg_ex['glutes_1'], 4))  

    elif user_input == "Upper Body".casefold():
      print(upper_body)

    if user_input == "Back and Biceps".casefold():
        print(random.sample(upper_ex['b_b'], 4))

    elif user_input == "Shoulders and Triceps".casefold():
        print(random.sample(upper_ex['s_t'], 4))

    elif user_input == "Cardio".casefold():
      print("You'll do 6 sets. 30 secs on/off. Rest 2 mins. between exercises.")
      print(cardio)

    elif user_input ==  "Core".casefold():
      print(core)       
   
print(f"You crushed it, {name}! Keep up the good work.")
