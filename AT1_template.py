#-----Statement of Authorship----------------------------------------#
#
#  This is an individual assessment task for QUT's teaching unit
#  ITD104, "Building IT Systems", C2, 2024.  By submitting
#  this code I agree that it represents my own work.  I am aware of
#  the University rule that a student must not act in a manner
#  which constitutes academic dishonesty as stated and explained
#  in QUT's Manual of Policies and Procedures, Section C/5.3
#  "Academic Integrity" and Section E/2.1 "Student Code of Conduct".
#
#  Put your student number here as an integer and your name as a
#  character string:
#
student_number = 11921111
student_name   = "Riya Murdhani"
#
#  NB: Files submitted without a completed copy of this statement
#  will not be marked.  All files submitted will be subjected to
#  software plagiarism analysis using the MoSS system
#  (http://theory.stanford.edu/~aiken/moss/).
#
#--------------------------------------------------------------------#



#-----Assessment Task 1 Description----------------------------------#
#
#  This assessment task tests your skills at processing large data
#  sets, creating reusable code and following instructions to display
#  a complex visual image.  The incomplete Python program below is
#  missing a crucial function.  You are required to complete this
#  function so that when the program runs it fills a grid with a symbol
#  of your choice, using data stored in a list to determine 
#  where to draw.  See the detailed assignment specifications documents
#  for full details.
#
#  Note that this assessable assignment is in multiple parts, simulating
#  incremental release of instructions by a paying "client".  This single
#  template file will be used for all parts and you should submit your final
#  solution as this single Python 3 file only, whether or not you complete
#  all requirements for the assignment.
#
#  This file relies on other Python modules but all of your code
#  must appear in this file only.  You may not change any of the code
#  in the other modules and you should not submit the other modules
#  with your solution.  The marker will use their own copies of the
#  other modules to test your code, so your solution will not work
#  if it relies on changes made to any other files.
#
#--------------------------------------------------------------------#  



#-----Preamble-------------------------------------------------------#
#
# This section imports necessary functions used to execute your code.
#
# You must NOT change any of the code in this section, and you may
# NOT import additional Python modules.

# Import standard Python modules needed to complete this assignment.
# Again, do NOT add any more import statements.
from turtle import *
from math import *
from random import *
from sys import exit as abort
from os.path import isfile

# Confirm that the student has declared their authorship
if not isinstance(student_number, int):
    print('\nUnable to run: No student number supplied',
          '(must be an integer), aborting!\n')
    abort()
if not isinstance(student_name, str):
    print('\nUnable to run: No student name supplied',
          '(must be a character string), aborting!\n')
    abort()

# Import the functions for setting up the drawing canvas
if isfile('AT1_config.py'):
    print('\nConfiguration module found ...\n')
    from AT1_config import *
else:
    print("\nCannot find file 'AT1_config.py', aborting!\n")
    abort()

# Define the function for generating data sets, using the
# imported raw data generation function if available, but
# otherwise creating a dummy function that just returns an
# empty list
if isfile('AT1_data_source.py'):
    print('Data generation module found ...\n')
    from AT1_data_source import raw_data
    def data_set(new_seed = randint(0, 99999)):
        print('Using random number seed', new_seed, '...\n')
        # set the seed
        seed(new_seed) 
        # return the random data set
        return raw_data() 
else:
    print('No data generation module available ...\n')
    def data_set(dummy_parameter = None):
        return []

#
#--------------------------------------------------------------------#



#-----Student's Solution---------------------------------------------#
#
#  Complete the assignment by implementing the dummy function below 
#  and adding any other functions needed to support it.
#  All of your solution code must appear in this section.  Do NOT put
#  any of your code in any other sections and do NOT change any of
#  the provided code except as allowed by the comments in the next section.
#
# All of your code goes in, or is called from, this function.
# Make sure that your code does NOT call function data_set (or
# raw_data) because it's already called in the main program below.

#function to draw hexagon in the center 
def minion():
    
#hexagon

    setheading(180)
    forward(60)
    setheading(60)
    pendown()
    color('light blue')
    begin_fill()
    for step in range(6):
        forward(60)
        right(60)
    end_fill()
    penup()
    
    
        
#minion body
    setheading(0)
    forward(60)
    setheading(90)
    forward(30)
    setheading(0)
    forward(30)
    setheading(90)
    color('yellow')
    begin_fill()
    circle(20,180)
    forward(40)
    circle(20,180)
    end_fill()

#eyes
    forward(45)
    setheading(270)
    forward(10)
    setheading(180)
    penup()
    forward(10)
    begin_fill()
    color('white')
    pendown()
    dot(15)
    end_fill()
    penup()
    forward(15)
    pendown()
    dot(15)

    penup()
    setheading(0)
    color('black')
    pendown()
    dot(5)

    penup()
    forward(12)
    pendown()
    dot(5)

#mouth
    penup()
    setheading(180)
    forward(15)
    setheading(270)
    forward(20)
    pendown()
    color('white')
    begin_fill()
    circle(10,180)
    left(90)
    forward(20)
    end_fill()

# clothes

    penup()
    color('blue')
    forward(10)
    setheading(270)
    forward(23)
    setheading(0)
    pendown()
    begin_fill()
    forward(15)
    left(90)
    forward(10)
    right(90)
    forward(10)
    right(90)
    forward(10)
    left(90)
    forward(10)
    penup()
    setheading(180)
    forward(34)
    setheading(270)
    pendown()
    circle(17, 180)
    end_fill()
    penup()

#legs
    setheading(270)
    forward(15)
    setheading(180)
    forward(7)
    setheading(270)
    pendown()
    color('black')
    begin_fill()
    forward(10)
    left(90)
    forward(10)
    setheading(20)
    circle(4,180)
    setheading(90)
    forward(12)
    end_fill()

    penup()
    setheading(180)
    forward(34)
    setheading(270)
    pendown()
    begin_fill()
    forward(20)
    left(90)
    forward(10)
    setheading(20)
    circle(4,180)
    setheading(90)
    forward(12)
    end_fill()
    penup()
# draw legend on the left hand side 
def legend():
    penup()
    goto(-((grid_width / 1.6) * horiz_spacing), -(vert_spacing // 1.5))
    minion()
    goto(-((grid_width / 1.7) * horiz_spacing), -(vert_spacing //0.4))
    write('minion',
              align = 'right', font = (label_font,16))
    
#draw compass on the right side 
def compass():
    goto((grid_width / 1.7) * horiz_spacing, -(vert_spacing //1.7))
    write('current\ndirection:\nNorth',
              align = 'left', font = (label_font, 16))
    
   
    

    
    
    
 
    
    

    

def visualise_data(movement):
    minion()
    legend()
    compass()
    home()
    if movement[0][2] == 'North':
        setheading(90)
    elif movement[0][2] == 'South':
        setheading(270)
    elif movement[0][2] == 'North east':
        setheading(45)
    elif movement[0][2]== 'North west':
        setheading(135)
    elif movement[0][2]== 'South east':
        setheading(315)
    elif movement[0][2]== 'South west':
        setheading(225)

        if movement[1][1]== 'Forward':
            forward(90)
            
        elif movement[1][1]== 'Forward and turn left':
            forward(60)
            left(60)
            
        elif movement[1][1]== 'Forward and turn right':
            forward(60)
            right(60)
    
        
            
        
    
    
     
    for i in range (movement[0][1]):
            forward(60)
            minion()
   
 

    
        
        
        
        
   
             
    


    
        
    

  
    

    
    


    

    



#--------------------------------------------------------------------#



#-----Main Program to Run Student's Solution-------------------------#
#
# This main program configures the drawing canvas, calls the student's
# function and closes the canvas.  Do NOT change any of this code
# except as allowed by the comments below.  Do NOT put any of
# your solution code in this section.
#

# Configure the drawing canvas
# ***** You can change the background and line colours, and choose
# ***** whether or not to draw the grid and other elements, by
# ***** providing arguments to this function call
create_drawing_canvas(canvas_title = "minion's playground", write_instructions = False) 

tracer(True)

# Call the student's function to process the data set
# ***** While developing your program you can call the
# ***** "data_set" function with a fixed seed below for the
# ***** random number generator, but your final solution must
# ***** work with "data_set()" as the function call,
# ***** i.e., for any random data set that can be returned by
# ***** the function when called with no seed
visualise_data(data_set()) # <-- no argument for "data_set" when assessed

# Exit gracefully
# ***** Do not change this function call
release_drawing_canvas(student_name)

#
#--------------------------------------------------------------------#
