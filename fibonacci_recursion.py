def fibonacci_function(number):
    if number == 0:
        return 0
    elif number == 1:
        return 1
    else:
        return fibonacci_function(number-1)+fibonacci_function(number-2)


user_input = eval(input("Enter an integer: "))
fibonacci_of_user_input = fibonacci_function(user_input)
print(fibonacci_of_user_input)