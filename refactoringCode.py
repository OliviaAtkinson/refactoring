feet = 6
inches = 3

def height_in_cm(feet, inches):
    ft_to_inch = feet * 12
    total_inch = inches + ft_to_inch

    cm = total_inch * 2.54
    print (cm)
    
height_in_cm(feet, inches)