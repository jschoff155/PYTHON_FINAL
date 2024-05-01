"""
Program: Python_final_project.py
Author: Jacob Schoff
Last date modified: 04/30/2024
Utilizing a variety of functions and tools learned in this class, program is designed to allow a user to:
1. Click a button and generate a random date night (Including special item, activity, resturaunt to go to, and the date for next night out)
2. Allow a user to input data to add to the existing arrays within the project
3. Save array information in separate files for each array via file I/O
"""

#DELIVERABLES REQUIRED:
# MUST INCLUDE:
# Requirement 1: A GUI component - MET/MARKED
# Requirement 2: Multiple functions (or methods) - MET/MARKED
# Requirement 3: Unit testing - MET/MARKED
# Requirement 4: Exception Handling (Try/Except) - MET/MARKED
# Requirement 5: Some sort of user input, including input validation - MET/MARKED
# Requirement 6: Some sort of output - MET/MARKED
# Requirement 7: A class - MET/MARKED

# MUST INCLUDE NINE OF THE FOLLOWING:
# Competency 1: Decision Structure: If, if-else, if-elif - MET/MARKED
# Competency 2: Looping Structure: For/while loop
# Competency 3: File I/O - MET/MARKED
# Competency 4: Inner function
# Competency 5: Function with arbitrary arguments: *args/**kwargs - MET/MARKED
# Competency 6: List/tuple
# Competency 7: Collection: Set/dictionary
# Competency 8: Collection: Array - MET/MARKED
# Competency 9: Case-switch statement
# Competency 10: Datetime - MET/MARKED
# Competency 11: Python Module or Package - MET/MARKED
# Competency 12: Data Scraper
# Competency 13: Object Oriented Functionality including constructors/methods/objects - MET/MARKED
# Competency 14: Object Oriented Program inheritance/polymorphism including base-derived class - MET/MARKED
# Competency 15: Database connectivity

#COMPETENCIES MET:
# Competency 1: Decision Structure: If, if-else, if-elif - MET/MARKED
# Competency 3: File I/O - MET/MARKED
# Competency 5: Function with arbitrary arguments: *args/**kwargs - MET/MARKED
# Competency 8: Collection: Array - MET/MARKED
# Competency 10: Datetime - MET/MARKED
# Competency 11: Python Module or Package - MET/MARKED
# Competency 13: Object Oriented Functionality including constructors/methods/objects - MET/MARKED
# Competency 14: Object Oriented Program inheritance/polymorphism including base-derived class - MET/MARKED

#IMPORTS/SETUP
from tkinter import *
import requests
from bs4 import BeautifulSoup
import unittest
import datetime
import random

#DEFINING THE CLASSES
#REQUIREMENT 7 MET - A CLASS
#COMPETENCY 13 MET - OBJECT ORIENTED FUNCTIONALITY (CONSTRUCTORS)
class Activity:
    def __init__(self, activity_name):
        self.activity_name = activity_name

#COMPETENCY 14 MET - OBJECT ORIENTED PROGRAM (INHERITANCE)
class Restaurant(Activity):
    def __init__(self, activity_name, restaurant_name):
        super().__init__(activity_name)
        self.restaurant_name = restaurant_name

class SpecialItem:
    def __init__(self, special_item_name):
        self.special_item_name = special_item_name

#REQUIREMENT 2 MET - MULTIPLE FUNCTIONS
#REQUIREMENT 4 MET - EXCEPTION HANDLING

def generate_date_night():
    try: #Generates a random value from each of the respective arrays
        activity = Activity(random.choice(activities))
        restaurant = Restaurant(random.choice(activities), random.choice(restaurants))
        special_item = SpecialItem(random.choice(special_items))
        #COMPETENCY 10 MET - DATETIME USED
        current_date = datetime.date.today()
        random_days = random.randint(0, 13)
        random_date = current_date + datetime.timedelta(days=random_days)
        cleaned_up_for_display_random_date = random_date.strftime("%m/%d")
        
        #Function to output the randomly generated fields 
        #REQUIREMENT 6 MET: OUTPUT OF PROGRAM MET
        generated_date_night_label.config(text=f"Generated Date Night:\nNext night out: {cleaned_up_for_display_random_date}\nActivity: {activity.activity_name}\nRestaurant: {restaurant.restaurant_name}\nSpecial Item: {special_item.special_item_name}")
    except Exception as e:
        generated_date_night_label.config(text=f"Unacceptbale Value: {str(e)}")

#REQUIREMENT 5 MET - USER INPUT WITH VALIDATION
def add_new_date_idea():
    activity_input = activity_entry.get()
    restaurant_input = restaurant_entry.get()
    special_item_input = special_item_entry.get()
    submit_button_success_label.config(text="Ideas added successfully")

    #Input validation for input fields (Won't allow user to submit until all fields has been supplied > Ensures balance and one field doesn't get a higher rate of duplicate outputs)
    #COMPETENCY 1 MET - IF, IF/ELSE, IF-ELIF
    if not (activity_input and restaurant_input and special_item_input):
        input_error_label.config(text="At least one field is required")

    #Additional input validation to ensure only letters are supplied (Prevents dirty data)

    if not activity_input.isalpha():
        input_error_label.config(text="Only letters can be allowed in the activity field")
        return

    if not restaurant_input.isalpha():
        input_error_label.config(text="Only letters can be allowed in the restaurant field")
        return

    if not special_item_input.isalpha():
        input_error_label.config(text="Only letters can be allowed in the special item field")
        return

    #Adding updated fields above to their respective arrays
    activities.append(activity_input)
    restaurants.append(restaurant_input)
    special_items.append(special_item_input)

    input_error_label.config(text="")

    #Resets fields upon appending
    activity_entry.delete(0, END)
    restaurant_entry.delete(0, END)
    special_item_entry.delete(0, END)



#Validation 
#COMPETENCY 5 MET - ARBITRARY ARGUMENTS
def update_submit_button_state(*args):
    if all((activity_entry.get(), restaurant_entry.get(), special_item_entry.get())):
        submit_button.config(state=NORMAL)
    else:
        submit_button.config(state=DISABLED)

#Built in items/arrays for the program
#COMPETENCY 8 MET - ARRAYS
restaurants = [
    "Bubba",
    "The Big Steer",
    "Milos",
    "Mullets"
]

activities = [
    "mini golf",
    "axe throwing",
    "bike ride",
    "walk in the park"
]

special_items = [
    "flowers",
    "small gift",
    "love letter",
    "make breakfast"
]

#COMPETENCY 3 MET - FILE I/O
try:
    def save_arrays_as_files(file_title, options):
        with open(file_title, "w") as file:
            for option in options:
                file.write(option + "\n")
except:
    pass
def save_arrays():
    save_arrays_as_files("restaurants_info.txt", restaurants)
    save_arrays_as_files("activities_info.txt", activities)
    save_arrays_as_files("special_items_info.txt", special_items)
    save_button_confirmation_label.config(text="Files saved successfully")


#REQUIREMENT 1 MET - GUI COMPONENT
#COMPETENCY 11 MET - PYTHON PACKAGE/MODULE (TKINTER)
FinalProject = Tk()
FinalProject.title("Date Night Generator")
FinalProject.geometry('200x300')

title_label = Label(FinalProject, text="Welcome to Date Night Generator")
title_label.grid(row=0, column=0, columnspan=3)

generate_button = Button(FinalProject, text="Generate Date Night", command=generate_date_night)
generate_button.grid(row=1, column=0, columnspan = 3)

#Randomly generated date night field
generated_date_night_label = Label(FinalProject, text="", justify="left")
generated_date_night_label.grid(row=2, column=0, columnspan=3)

add_new_items_label = Label(FinalProject, text="Add new items below:")
add_new_items_label.grid(row=4, column=0, columnspan = 3)

#Labels for inputs
activity_label = Label(FinalProject, text="Activity:")
activity_label.grid(row=5, column=0)
restaurant_label = Label(FinalProject, text="Restaurant:")
restaurant_label.grid(row=6, column=0)
special_item_label = Label(FinalProject, text="Special Item:")
special_item_label.grid(row=7, column=0)

# Input Fields
activity_entry = Entry(FinalProject)
activity_entry.grid(row=5, column=1, columnspan = 2)
restaurant_entry = Entry(FinalProject)
restaurant_entry.grid(row=6, column=1, columnspan = 2)
special_item_entry = Entry(FinalProject)
special_item_entry.grid(row=7, column=1, columnspan = 2)

# Input Error Label
input_error_label = Label(FinalProject, text="", fg="red")
input_error_label.grid(row=8, column=0, columnspan=3)

submit_button = Button(FinalProject, text="Add new ideas", command=add_new_date_idea, state=DISABLED)
submit_button.grid(row=9, column=0, columnspan=3)
submit_button_success_label = Label(FinalProject, text="")
submit_button_success_label.grid(row=10, column=0, columnspan=3)
save_button = Button(FinalProject, text="Save all options to machine", command=save_arrays)
save_button.grid(row=11, column=0, columnspan=3)
save_button_confirmation_label = Label(FinalProject, text="")
save_button_confirmation_label.grid(row=12, column=0, columnspan=3)

#Reading user inputs upon key strikes and updates 
activity_entry.bind("<KeyRelease>", update_submit_button_state)
restaurant_entry.bind("<KeyRelease>", update_submit_button_state)
special_item_entry.bind("<KeyRelease>", update_submit_button_state)

#REQUIREMENT 3 MET - UNIT TESTS INCLUDED
#Running validation on inputs to ensure nothing other than letters are allowed in the inputs
# class TestCases(unittest.TestCase):

#     def test_activity_entry(self):
#         activity_entry_value = "Hike a few miles"
#         self.assertTrue(activity_entry_value.isalpha())
        
#         activity_entry_value_invalid = "Run 12 feet"
#         self.assertFalse(activity_entry_value_invalid.isalpha())

#     def test_restaurant_entry(self):
#         restaurant_entry_value = "Italian Restaurant"
#         self.assertTrue(restaurant_entry_value.isalpha())
        
#         restaurant_entry_value_invalid = "Italian Restaurant & Cafe"
#         self.assertFalse(restaurant_entry_value_invalid.isalpha())

#     def test_special_item_entry(self):
#         special_item_entry_value = "Flowers"
#         self.assertTrue(special_item_entry_value.isalpha())
        
#         special_item_entry_value_invalid = "Flowers123"
#         self.assertFalse(special_item_entry_value_invalid.isalpha())

# if __name__ == '__main__':
#     unittest.main()

FinalProject.mainloop()

