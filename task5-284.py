
# Initializing my lists
positive_list = []
negative_list = []
zero_list = []

while True:
    user_input = input("Please enter a number(blank to quit): ")


# Checking if the user wants to stop the program
    if user_input == "":
        break

# Converting the input for sorting
    user_number = int(user_input)

    if user_number > 0:
        positive_list.append(user_number)

    elif user_number == 0:
        zero_list.append(user_number)

    elif user_number < 0:
        negative_list.append(user_number)


# The "*" before the lists removes the brackets and commas
print("\nThe numbers were:")
print(*positive_list, *zero_list, *negative_list)

