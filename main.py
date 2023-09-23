def list_options():
    print('menu options:')
    print('1. Sum')
    print('2. Subtract')
    print('3. Multiply')
    print('4. Division')
    print('5. Calculate triangle area')
    print('6. Calculate circle area')
    print('7. Calculate rectangle area')
    print('8. Exit')
    print('Please enter the number of operation you want to do')


def sum():
    print('Enter first number')
    first_num = int(input())
    print('Enter second number')
    second_num = int(input())
    result = first_num+second_num
    print("The result is: ", result)


def subtract():
    print('Enter first number')
    first_num = int(input())
    print('Enter second number')
    second_num = int(input())
    result = first_num-second_num
    print("The result is: ", result)


def multiply():
    print('Enter first number')
    first_num = int(input())
    print('Enter second number')
    second_num = int(input())
    result = first_num * second_num
    print("The result is: ", result)


def division():
    print('Enter first number')
    first_num = int(input())
    print('Enter second number')
    second_num = int(input())
    result = first_num / second_num
    print("The result is: ", result)


def calculate_triangle_area():
    print('Enter base')
    base = int(input())
    print('Enter length')
    length = int(input())
    result = base * length
    print("The result is: ", result)


def calculate_circle_area():
    print('Enter radius')
    radius = int(input())
    result = 3.14*radius**2
    print("The result is: ", result)


def calculate_rectangle_area():
    print('Enter length')
    length = int(input())
    print('Enter width')
    width = int(input())
    result = length * width
    print("The result is: ", result)


list_options()
option_number = int(input())

if option_number == 1:
    sum()
elif option_number == 2:
    subtract()
elif option_number == 3:
    multiply()
elif option_number == 4:
    division()
elif option_number == 5:
    calculate_triangle_area()
elif option_number == 6:
    calculate_circle_area()
elif option_number == 7:
    calculate_rectangle_area()
elif option_number == 8:
    exit()
else:
    print('The option number is incorrect')



