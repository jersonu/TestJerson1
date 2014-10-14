""" 
Welcome to Codeskulptor's visualization mode (Viz mode)!
Viz mode runs in Chrome, Firefox or Safari

Click the wrench button above to active Viz mode, then
click the triangle button to visualize the execution of
the demo program
"""

def list_minimum(numbers):
    """
    Compute the minimum of a list of numbers
    """
    
    min_num = float("inf")
    for num in numbers:
        if num < min_num:
            min_num = num  # Set breakpoint on this line
    return min_num

example_list = [4.6, 5.9, 2.1, 5.7, 1.1, 8.3]
print "An example list is", example_list
print 
minimum_number = list_minimum(example_list)
print "The minimum of this example list is", minimum_number



# The light blue bars in the code editor and console
# indicate the current active line/event. 

# Navigate the execution trace of your program using 
# the next/prev statement buttons. 

# Click a line number to set a breakpoint for a line
# Navigate between execution trace breakpoints using 
# the next/prev breakpoint/event buttons
