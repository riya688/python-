
#-----Module Description - Dataset Generation-----------------------#
#
#  This module contains a function needed for Assessment Task 1 in
#  QUT's teaching unit ITD104 "Building IT Systems".  You should put
#  a copy of this file in the same folder as your solution to the
#  assignment.  The necessary element will then be imported
#  into your program automatically.
#
#  NB: Do NOT make any changes to this module and do NOT submit a
#  copy of this file with your solution.  Changes made to this
#  module will have no effect when your assignment is graded because
#  the markers will use their own copy of this file.  If your program
#  relies on changes made to this file it will fail to work when
#  assessed.
#
#--------------------------------------------------------------------#



#-----Preamble-------------------------------------------------------#
#
# This section imports necessary functions used for generating the
# dataset.
#

# Import standard Python functions for making "random" choices
from random import randint, choice

#
#--------------------------------------------------------------------#



#-----Dataset Function for Assessing Your Solution------------------#
#
# The function in this section is called by the assignment template
# to generate the datasets used by your program.

# The following function creates a random dataset defining the
# overall image to draw.  Your program must work for ANY dataset that
# can be produced by this function.  The results returned by calling
# this function will be used as the argument to your data visualisation
# function during marking.  For convenience during code development
# and marking this function also prints the dataset generated to the
# shell window.  NB: Your solution should not print anything else to
# the shell.  Make sure any debugging calls to the "print" function
# are disabled before you submit your solution.
#
def raw_data():

    # Define the possible ways the object can move and turn
    moves = ['Forward', 'Forward and turn left', 'Forward and turn right']
    # Define the possible initial orientations
    directions = ['North', 'North east', 'South east',
                  'South', 'South west', 'North west']

    # Choose the number of moves
    num_moves = randint(1, 10)
    # Choose the object's initial energy level
    # (which mustn't exceed the number of moves)
    energy = randint(1, num_moves)
    # Choose the object's initial orientation
    direction = choice(directions)

    # Keep track of how many moves have been created in total
    move_no = 0

    # Initialise the dataset with the special first move
    random_moves = [[move_no, energy, direction]]

    # Create the remaining moves
    while move_no < num_moves:
        # Increment move number
        move_no = move_no + 1
        # Choose which way the object moves and turns
        move = choice(moves)
        # Add the new move to the dataset
        random_moves.append([move_no, move])

    # Print the whole dataset to the shell window, laid out
    # nicely, one move per line
    print("The moves to visualise are:\n")
    print(str(random_moves).replace('],', '],\n'))
    
    # Return the dataset to the caller
    return random_moves

#
#------------------------------------------------------------------------------#



#------------------------------------------------------------------------------#
# Some "fixed" datasets
#
# Developing code when the underlying dataset changes randomly can
# be difficult.  To help you develop your code you can temporarily
# provide the call to the data generation function at the bottom of
# the assignment template file with a "seed" value which will force
# it to produce a known dataset.  Of course, having completed your
# solution, your program must work for any list that can be returned
# by calling the data generation function with no argument.
#
# Some examples of useful seed numbers follow.  Of course, you are
# free to choose other seed values to help you debug your code.
#
# ---------
# Datasets where the object completes the moves:
#
# 27314 - object completes the 1 move, ending in cell 6D, facing North
#
# 68954 - object completes the 2 moves, ending in cell 8D, facing North West
#
# 13674 - object completes the 3 moves, ending in cell 1C, facing South West
#
# 81534 - object completes the 8 moves, ending in cell 2D, facing North
#
# ---------
# Datasets where the object runs out of energy:
#
# 95296 - object only has energy for 2 moves, ending up exhausted in cell 2F,
#         facing South
#
# 90319 - object runs out of energy after 3 moves, ending up exhausted 
#         in cell 7G, facing North
#
# 37056 - object runs out of energy after 4 moves, ending up exhausted 
#         in cell 5I, facing North East
#
# 78082 - object runs out of energy after 4 moves, ending up exhausted
#         in cell 2B, facing South East
#
# 53007 - object is exhausted in cell 6H after 3 moves, facing South East
#
#
# ---------
# Datasets where the object moves outside the grid:

# 78669 - object exits the grid on the 5th move, last seen in cell 8H,
#         facing North
#
# 78655 - object exits the grid on the 6th move, last seen in cell 1A,
#         facing North West
#
# 71923 - object exits the grid on the 6th move, last seen in cell 9I,
#         facing North 
#
# 76312 - object goes straight out the top of the grid in its 3rd move, 
#         last seen in cell 9E facing North
#
# 90944 - object goes straight out the bottom of the grid in its its 3rd move, 
#         last seen in cell 1E facing South
#
# 20162 - object exits the bottom of grid in its 3rd move, last seen in cell 2F,
#         facing South
#
# 6449 -  object exits from left of grid in its 5th move, last seen in cell 5A, 
#         facing South West
#
# 23011 - object exits at top of grid in its 5th move, last seen in cell 8F, 
#         facing North
#
# 61202 - object exits from right of grid in its 5th move, last seen in cell 7I,
#         facing South East
#
#
# ---------
# Some long paths followed:
#
# 89444 - object walks a full circle, runs out of energy, and ends up
#         in cell 3E, facing North 
#
# 22745 - object completes all 9 moves and finishes in cell 1C
#         facing South West
#
# 26907 - object completes 9 moves but ends up exhausted in cell 8F,
#         facing North East
#
#
#------------------------------------------------------------------------------#

