my_list = [0, 1]

for i in range(2, 30):
    value = (my_list[i-1]) + (my_list[i-2])
    my_list.append(value)
    
print('Fibonacci sequance:')

for i in range(len(my_list)):
    print("{}{} {}" .format (i+1, '.', my_list[i]))