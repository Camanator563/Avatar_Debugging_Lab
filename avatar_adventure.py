
#? Question answers
# Breakpoints are helpful because it makes you check every bit of code to see if any errors are there.
# pdb helped me with it cause that was the import that made it so that the breakports would actually work.
# I think that the print function is the most useful because it allows me to check what every variable is equal to at different points of code.# Avatar Adventure Debugging Lab

#! The Code
import pdb # Import the debugger


# Code continues...

# Characters and elements
class Character:
    def __init__(self, name, element):
        self.name = name
        self.element = element


    def introduce(self):
        return f"My name is {self.name}, and I am a {self.element} bender."


# Create character objects
aang = Character("Aang", "Air")
katara = Character("Katara", "Water")
toph = Character("Toph", "Earth")

# Incorrect function to test with pdb
def journey_to_element(Character):
    if Character.element == "Air":
        return "Aang flies with his glider."
    elif Character.element == "Water":
        return "Katara bends water to travel."
    elif Character.element == "Earth":
        return "Toph creates earth walls to move forward."
    else:
        return "This character does not have an elemental power!"

# Simulate the journey
print(aang.introduce())
print(journey_to_element(aang))
print(katara.introduce())
print(journey_to_element(katara))
print(toph.introduce())
print(journey_to_element(toph))
