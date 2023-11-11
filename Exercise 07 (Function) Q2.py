# Exercise 07 Question 02
# Write a Python program where users input two numbers and choose an 
# operation (+, -, *, /, **). Use lambda functions for calculations. If division is 
# chosen and the second number is zero, replace it with one, notify the user, and 
# proceed. The program should handle invalid operations gracefully. This program 
# should be repeated until user write “exit”.



# Exit completely
def exit_program():
    import sys
    print("-----------------bye-------------------")
    print(".... Thank you to choose my program ....")
    sys.exit(0)

# Check float
def is_float(num):   
    try:
        float(num)
        return True
    except ValueError:
        return False

# Alpha or mixes alpha and digit ==> True  "." or digit ==> False

def is_string(num):    
    for i in num:
        if i.isalpha():
            return True
            break
    return False

# Check number (int or float)

def is_number(num):
    if is_string(num):
        return False
    elif is_float(num):
        return True
    return False

# input from user 2 Numbers and if not valid, repeat input until exit and return numbers as a list

def input_number():
    numb = []
    i = 1
    while 1:
        num = input(f"Please enter your number {i} [or press x to exit]: ")
        if num.lower() == "x":
            exit_program()
        while 1:
            if not is_number(num):
                print(">>> Error : You have to enter a number")
                num = input(f"Please enter your number {i} again [or press x to exit]: ")
                if num.lower() == "x":
                    exit_program()
                continue
            numb.append(num)
            break
        i += 1
        if i>2 :
            break
    n1 = float(numb[0])
    n2 = float(numb[1])
    return(n1,n2)

# --------------- main --------------

sum_numbers = lambda x, y : x + y
minus_numbers = lambda x, y : x - y
multipl_numbers = lambda x, y : x * y
divide_numbers = lambda x, y : x / y

i = 1
while 1:
    x,y = input_number()
    while 1:
        opr = input("Please enter your number operation(+ - * /) [or press x to exit]: ")
        if opr.lower() == "x":
            exit_program()
        elif opr == "+":
            result = sum_numbers(x,y)
            break
        elif opr == "-":
            result = minus_numbers(x,y)
            break
        elif opr == "*":
            result = multipl_numbers(x,y)
            break
        elif opr == "/":
            if y == 0.0:
                print("you entered 0 for the second number ==> it replaces with 1")
                y = 1.0
            result = divide_numbers(x,y)

            break
        else:
            print(">>> Error : You have to enter a operation(+ - * /) ")
            opr = input(f"Please enter your oeration again [or press x to exit]: ")
            if opr.lower() == "x":
                exit_program()
                
        i+=1 
    print (f"The result {x} {opr} {y} = {result}")
    