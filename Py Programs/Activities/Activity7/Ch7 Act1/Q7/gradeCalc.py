# Calculating a Letter Grades
def main():
    g = float(input("Please enter a number grade. "))
    if g < 0 or g > 100:
        print("Please enter a valid integer number grade. ")
    else:
        if g >= 90:
            print("Letter grade is an A.")
        elif g > 80 and g <= 89:
            print("Letter grade is an B.")
        elif g > 70 and g <= 79:
            print("Letter grade is an C.")
        elif g > 60 and g <= 69:
            print("Letter grade is an D.")
        else:
            print("Letter grade is an F.")
main()
