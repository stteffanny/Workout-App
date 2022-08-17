# run me in your terminal
# by typing python3.10 workout.py
# and pressing enter

import random

def welcome():
  print("Welcome to your personalized fitness App." " " "(◕‿◕✿)")
  print("--------")

def instructions():
  print("Instructions: You'll do 4 sets / 12 reps per exercise.")
  print("Please take a 45 second rest between sets.")
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

lower_body = {'Quads', 'Hamstrings', 'Glutes'}

upper_body = {'Back and Biceps', 'Shoulders and Triceps'}

quads = ["Barbell Squats", "Lunges", "Pigeon Lunges", "Sumo Leg Press", "Narrow Leg Press", "Leg Extensions", "Bulgarian Split Squats"]

hamstrings = ["Romanian Deadlifts", "Sumo Deadlifts", "Lying Leg Curl", "Swiss-Ball Leg Curl", "Hip-Thrusts", "Stiff Leg Deadlifts", "Single-Leg Deadlifts"]

glutes = ['Barbell Hip-Thrusts', 'Bulgarian Split Squats', 'Frog Pump', 'Cable Kickbacks', 'Banded Hip-Thrusts', 'Banded Frog Kicks', 'Single-leg Hip-Thrusts']

back_biceps = ['Lat Pulldowns', "Assited Push Ups", "Barbell Bicep Curls", "Trx Inverted Rows" "Seated Rows", "Bent-Over Rows", "Assisted Pull-Ups", "T-Bar Rows", "Single-Arm Dumbbell Row"]

shoulders_triceps = ['Shoulder Taps', 'Seated Arnold Press', 'Dumbbell Chest Press','Seated Front Raises', 'Dumbbell Lateral Raises', 'Cable Single Arm Pull Downs', 'Push Ups', 'Cable Tricep Pushdowns']

terminate = False

while not terminate:
    print("--------")

    user_input = input('> ') 

    if user_input == "quit":
      terminate = True

    if user_input == "Lower Body".casefold():
      print(lower_body)  

    elif user_input == "Quads".casefold():
      print(random.sample(quads, 4))

    elif user_input == "Hamstrings".casefold():
      print(random.sample(hamstrings, 4))  

    elif user_input == "Glutes".casefold():
      print(random.sample(glutes, 4))  

    elif user_input == "Upper Body".casefold():
      print(upper_body)

    if user_input == "Back and Biceps".casefold():
        print(random.sample(back_biceps, 4))

    elif user_input == "Shoulder and Triceps".casefold():
        print(random.sample(shoulders_triceps, 4))

    elif user_input == "Cardio".casefold():
      print("You'll do 6 sets. 30 secs on/off. Rest 2 mins. between exercises")
      print("Steady State Bike", "Elliptical Sprints", "Med Ball Slams", 'Box Jumps', "Steady Skate Bike")

    elif user_input ==  "Core".casefold():
      print("30 sec Plank", "Leg Raises", "30 sec Oblique planks", "Anchored Russian Twists", "Toe Taps", 'Mountain Climbers')       
   
print("You crushed it! Keep up the good work.")
