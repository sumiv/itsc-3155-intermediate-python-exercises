# Nathan Laney, Kaitlyn Finberg, Sumi Verma, Tyler Minnis, Honna Sammos

# Write a function that takes in a list data structure as input. 
# The function should create a new list and only include unique elements of the inputted list. 
# Under the function, write code that calls the function with a test list like so and print out the result. 
# Remember that your code should work for all lists of integers, not just the sample test here.

def get_unique_list(ex_list):
    unique_list = []
    for i in ex_list:
        if i not in unique_list:
            unique_list.append(i)
    return unique_list

my_list = [1, 2, 3, 2, 1, 4]
unique_list = get_unique_list(my_list)
print(unique_list)