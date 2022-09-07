# Nathan Laney, Kaitlyn Finberg, Sumi Verma, Tyler Minnis, Honna Sammos

# Write a function that takes in two dict data structures as input. 
# Both dicts map str->int (the keys are strings and the values are integers). 
# The function should compute a new dict which combines the two dicts by summing the values for the common keys. 
# Keys that are not common should be left out. Use the following code to test your function, 
# but remember that your function should for all str->int dict inputs, not just the test here.

def get_combined_dict(dict_one, dict_two):
    common_dict = {}
    for key in dict_one:
        if key in dict_two:
          common_dict[key] = dict_one[key] + dict_two[key]  
    return common_dict

my_dict_1 = {'a': 5, 'b': 12, 'c': 3, 'd': 9}
my_dict_2 = {'b': 4, 'c': 9, 'd': 10, 'e': 16}
combined_dict = get_combined_dict(my_dict_1, my_dict_2)
print(combined_dict)