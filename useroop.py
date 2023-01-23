"""
Priyanka Gorentla
Date January 23, 2023
Domain: Yoga
This task is to know about yoga institues and trainings given to the students and monitering the weight's of them.
Build a PyBuddy to extend a welcome.

Uses:

- new Python 3.7 data classes
- list compreshensions for concise processing
- multiline strings -
- some are indented because all the way left seems ugly.

"""

# import from dataclasses to make our job even easier
from dataclasses import dataclass, field

import datetime
from enum import Enum
import statistics
import math
import random
import doctest


class Species(Enum):
    DOG = 1
    CAT = 2
    ELF = 3
    ORC = 4


# Add the @dataclass decorator to let Python do more of the work
# Notice what changes.

"""
>>> get_varying_weights([66.7, 70, 65, 77.2, 62.1])
68.2

"""


@dataclass
class PyBuddy:
    """PyBuddy data class for creating a study buddy.

    Doctest examples and expected outputs:

    """

    # With a data class, we just name each field and provide the type.
    # Include a default value in case something is not provied.
    name: str = "Unknown"
    species: Species = 1
    num_legs: int = 4
    weight_kgs: float = 9.999999999
    is_available: bool = True
    skill_list: list = field(default_factory=list)
    create_date = datetime.datetime.now()
    inst_location: list = field(default_factory=list)
    gen:list = field(default_factory=list)
    typ:list = field(default_factory=list)
    varying_weights: list = field(default_factory=list)
    max_wei: float =""
    min_wei: float =""
    double_weight: float =""
    mode_weight: float = ""
    cube_weight: float =""

    def get_age_string(self):
        """Return a string with our age."""
        return str(datetime.datetime.now() - self.create_date)

    def get_availability_string(self):
        """Return a message based on availability."""
        if self.is_available:
            return "I'm available for tutoring."
        else:
            return "I'm already helping others learn Python."

    def get_skills_string(self):
        """Return a nicely formatted string of skills."""
        # use concise list comprehension syntax
        return "".join([str(f"  - {elem}\n") for elem in self.skill_list])

    def get_varying_weights(self):
         """average weight of the person """
         mean_weight = round(statistics.mean(self.varying_weights), 2)
         return mean_weight

    def get_mode(self):
        """mode"""
        mode_weight = round(statistics.mode(self.varying_weights), 2)
        return mode_weight

    def get_cube_root_of_weight(self):
        "cube roor of weight"
        cube_weight = math.floor((round(statistics.mode(self.varying_weights), 2)**3))
        return cube_weight
        
    def max_weight(self):
        """Maximum weight"""
        max_wei = min(self.varying_weights)
        return max_wei

    def min_weight(self):
        """Weight after joining in Yoga"""
        min_wei = max(self.varying_weights)
        return min_wei


    def display_welcome(self):
        """Display a welcome message from this instance."""

        print(
            f"""
Welcome, I'm a new PyBuddy.
{self.to_string()}
You'll need curiosity, the ability to search the web, 
and the tenacity and resourcefulness
to solve all kinds of challenges.
Let's get started! 

        """
        )

    def to_string(self):
        """Return a custom string describing this instance"""

        # Use an f-string (aka 'formatted string literal')
        # Use curly braces to switch into code that will be executed."
        # Wrap it all in parentheses so we can move the left side.
        return f"""
I'm {self.name}.
Average weight of me from last 6 months {self.get_varying_weights()}.
I have {self.species} with {self.num_legs} legs.
weigh {self.weight_kgs:.2f} kgs.
Age is:{self.get_age_string()}.
I know yoga skills:
{self.get_skills_string()}
Before joining into yoga my weight was: {self.max_weight()}.
After joining into yoga my weight was : {self.min_weight()}.
Mode of the weight : {self.get_mode()}.
Double age : {self.get_double_weight()}.
Triple age : {self.get_cube_root_of_weight()}.
I have been into one of the yoga institutes: {self.get_inst_location()}.
Yoga will be trained to genders : {self.get_gen()}.
There will 2 types of people : {self.get_typ()}.
"""

    def get_inst_location(self):
        """Yoga institutes are in these perticular locations"""
        loc = random.choice(self.inst_location)
        return loc
    
    def get_gen(self):
        for gend in self.gen:
            """Yoga institutes can train to male,female and unisex people"""
            return self.gen
    def get_typ(self):
        for typs in self.typ:
           """Yoga institutes has two types of people - Experienced and Fresher"""
           return self.typ
    print(get_typ.__doc__)      
    
    def get_double_weight(self):
           "double weight"
           double_weight = math.ceil((round(statistics.mode(self.varying_weights), 2)*2))
           return double_weight

    print(math.__doc__)
    print(math.ceil.__doc__)       



# -------------------------------------------------------------
# Call some functions and execute code!

# if this is the main file being run, do this:
if __name__ == "__main__":

    # Create an instance of a PyBuddy
    alice = PyBuddy(
        "vijay",
        Species.CAT,
        4,
        8.123456,
        True,
        ["holdingBreath", "Pranayama", "SuryaNamaskar", "Asans", "kapalibath"],
        [
            "FL_Jacksonville",
            "NJ_Edison",
            "NC_Charlotte",
        ],
        ["Female","Male","Unisex"],
        ["Experienced","New Joinee"],
        [69.2, 73, 79, 77.2, 84],
    )

    # Call the buddy's welcome() method
    alice.display_welcome()

    # Create another instance of a PyBuddy
    # using named arguments so it's clear what we're doing
    rex = PyBuddy(
        name="Priyanka",
        species=Species.DOG,
        num_legs=4,
        weight_kgs=10.437241,
        is_available=True,
        skill_list=["Pranayama", "SuryaNamaskar", "Asans", "kapalibath", "holdingBreath"],
        inst_location=["Florida_Jacksonville", "NewJersey_Edison", "NorthCarolina_Charlotte"],
        gen=["Female","Male","Unisex"],
        typ=["Experienced","New Joinee"],
        varying_weights=[66.7, 70, 65, 77.2, 62.1],
        min_wei="",
        max_wei="",
        double_weight="",
        cube_weight="",
        mode_weight="",
    )
       
    rex.display_welcome()

    print("Running doctest.testmod() function to unit test our code")
    print("===========================================================")
    print()
    doctest.testmod()
    print()  
    print(math.__doc__)
    print(math.ceil.__doc__)   