message = "Hello, World!"
print(message)

fundamental = "Python is fun!"
print(fundamental)


def radius():
    r = 5
    area = 3.14159 * r ** 2
    print(area)
    
    

def height_to_cm(feet, inches):
        total_inches = feet * 12 + inches
        cm = total_inches * 2.54
        return cm
height_cm = height_to_cm(5, 7)
print(f"{height_cm} cm")


def round_up_or_down(number):
    if number < 500:
        number_rounded = 1000
    else:
        last_three_digits = number % 1000
        if last_three_digits >= 500:
            number_rounded = number + (1000 - last_three_digits)
        else:
            number_rounded = number - last_three_digits
    print(number_rounded)

# Example usage
round_up_or_down(499)  # Output: 1000
round_up_or_down(500)  # Output: 1000
round_up_or_down(999)  # Output: 1000
round_up_or_down(1000) # Output: 1000
round_up_or_down(1499) # Output: 1000
round_up_or_down(1500) # Output: 2000