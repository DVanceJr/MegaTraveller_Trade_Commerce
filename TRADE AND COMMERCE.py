# TRADE AND COMMERCE
# David Vance
# 2 October 2024

"""The purpose of this program is to automate the Trade and Commerce routines
for the Traveller and MegaTraveller Roleplaying Games."""


# INITIALIZE
# Define functions and modules, initialize variables, input values

def from_chart(chart_list, chart_index):
    """Determine the dice combination from a chart using the correct index"""
    dice_matrix = chart_list[chart_index]   
    return dice_matrix

def roll_from_chart(chart_value):
    """Parse the dice expression and pass to roller, return dice result"""
    main_die = 0
    mod_die = 0
    mod_number = 0
    roll_result = 0
    math_expression = ""

    main_die = int(chart_value[:1])  # Get the leftmost value - always dice

    if main_die > 0 and chart_value[-1] != "D":  # Process for simple modifier
        mod_number = int(chart_value[-1])  # Get the simple modifier
        math_expression = chart_value[-2]  # Get the math expression
        # roll_result = roll_dice(main_die, math_expression, mod_die, mod_number)
    
    elif main_die > 0 and chart_value[-1] == "D":  # Process for a die roll modifier
        mod_die = int(chart_value[-2])  # Get the second die count
        math_expression = chart_value[-3]  # Get the math expression
        # roll_result = roll_dice(main_die, math_expression, mod_die, mod_number)

    print(main_die, math_expression, mod_die, mod_number)

    return    


# PROCESSING
# 
# Set the chart to be rolled and its index 

high_pass_list = ['0', '0','1D-1D', '2D-2D', '2D-1D', '2D-1D', '3D-2D', '3D-2D', '3D-D1', '3D-1D', '3D-0D']
source_pop = 8

chart_value = from_chart(high_pass_list, source_pop) # Returns the chart value
print('Passing ', chart_value, ' to roller')

high_passengers = roll_from_chart(chart_value)


# TERMINATIONS
# Print final results, end program
