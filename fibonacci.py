import sys 

def create_fibonacci_list(given_list_size, starting_list):
    for i in range(2, given_list_size):
        value = (starting_list[i-1]) + (starting_list[i-2])
        starting_list.append(value)

def print_list(number_ajust_to_left, number_ajust_to_right):
    print("{} {}" .format(number_ajust_to_left, number_ajust_to_right))

def create_strings_from_numbers_to_print(list_size, my_list):
    for i in range(len(my_list)):
        lengh_last_number = len(str(my_list[list_size-1]))
        my_list_current_number = str(my_list[i])
        number_to_right = my_list_current_number.rjust(lengh_last_number)

        index_track = (str(i+1) + '.')
        number_ajust_to_left = index_track.ljust(len(str(list_size)+'1'))

        print_list(number_ajust_to_left, number_to_right)

list_size = eval(input())
my_list = [0, 1]

create_fibonacci_list(list_size, my_list)

print('Fibonacci sequance:')

create_strings_from_numbers_to_print(list_size, my_list)