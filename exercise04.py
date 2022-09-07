# Nathan Laney, Kaitlyn Finberg, Sumi Verma, Tyler Minnis, Honna Sammos

# Take in 5 int inputs from the user and add them together. 
# The catch is that you can no longer assume that what the user enters is a valid int. 
# If the user enters an invalid input, print an error message 
# and make the user input the int again until all 5 int values are entered correctly. 
# Print the resulting sum.

sum = 0
index = 1

while index < 6:
    try:
        user_input = int(input(f'Enter int #{index}: '))
        index = index + 1
    except ValueError:
        print(f'Invalid input. Please enter an int.')
        continue
    else:
        sum += user_input

print('Your sum is',sum)