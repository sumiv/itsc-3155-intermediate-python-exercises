# Nathan Laney, Kaitlyn Finberg, Sumi Verma, Tyler Minnis, Honna Sammos

# Take in a string from the user and pass it as input to a function. 
# Have the function return a dict which keeps count of each letter (in lowercase) in the string, 
# excluding spaces. Print out this dict.

def char_count(my_input):
    my_dict = {}
    given_spaces = my_input.lower()
    given = given_spaces.replace(" ", "")
    given_list = [*given]
    for i in range(0, len(given)):
        my_dict[given_list[i]] = given.count(given_list[i])
    return(my_dict)

user_input = input("Enter a string: ")
print(char_count(user_input))