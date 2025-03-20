# ---------------------------------------------------------------------------- #
#                                                                              #
# 	Module:       main.py                                                      #
# 	Author:       31077                                                        #
# 	Created:      3/7/2025, 11:45:49 AM                                        #
# 	Description:  V5 project                                                   #
#                                                                              #
# ---------------------------------------------------------------------------- #

# Library imports
from vex import *

brain = Brain()
controller_1 = Controller(PRIMARY)

# Robot configuration code: copy or add config code for motors, drivetrain, etc. here


# Define any custom functions here; you can then use these functions in your auton or driver control code




####################################### Code for Auton ###################################################
def autonomous():
    brain.screen.clear_screen()
    brain.screen.print("autonomous code")
    # place automonous code here


####################################### Code for Driver Control ##########################################
def user_control():
    brain.screen.clear_screen()
    brain.screen.print("driver control")
    # place driver control in this while loop
    while True:
        # Arcade Drive or Tank Drive: copy the correct code from Snippets or write your own 


        # Continue your driver control code here



        wait(20, MSEC)




####################################### Do Not Change Code Below ##########################################
# create competition instance
comp = Competition(user_control, autonomous)

# actions to do when the program starts
brain.screen.clear_screen()