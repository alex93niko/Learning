# This function draws a rectangle in the terminal with the specified height and width parameters
def draw_func(width, height):

    if width < 2 or height < 2:  # Minimal size check
        print("Error! width or height is too small, need >= 2 .")
        quit()

    print("*" * width)  # Drawing the first line
    for i in range(height-2):  # Drawing the columns
        print("*" + " " * (width - 2) + "*")
    print("*" * width)  # Drawing the last line


draw_func(1, 2)  # Function_call
