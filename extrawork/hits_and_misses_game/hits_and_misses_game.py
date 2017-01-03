import random

lucky_number = random.randint(1,9999)
print(lucky_number)


points_for_getting_units = 0
points_for_getting_tens  =  0
points_for_getting_hundrands = 0
points_for_getting_thousands = 0

missed = 0
total_found = 0

while  total_found != 4:



    missed += 1

    user_input_lucky_number = int(input("guess the lucky number: "))


    computer_input_units = int((lucky_number / 1000))
    computer_input_tens = int((lucky_number / 100 -(computer_input_units * 10 ) ))
    computer_input_hundrands = int((lucky_number / 10- (computer_input_units * 100) - computer_input_tens *10  ))
    computer_input_thousands = int((lucky_number / 1- (computer_input_units * 1000) - computer_input_tens * 100)- computer_input_hundrands * 10)


    user_input_units = int((user_input_lucky_number / 1000))
    user_input_tens = int((user_input_lucky_number / 100 -(user_input_units * 10 ) ))
    user_input_hundrands = int((user_input_lucky_number / 10- (user_input_units * 100) - user_input_tens *10  ))
    user_input_thousands = int((user_input_lucky_number / 1- (user_input_units * 1000) - user_input_tens * 100)- user_input_hundrands * 10)



    if user_input_units  == computer_input_units:
        points_for_getting_units = 1



    if user_input_tens == computer_input_tens:
        points_for_getting_tens =1


    if user_input_hundrands  == computer_input_hundrands:
        points_for_getting_hundrands = 1



    if user_input_thousands == computer_input_thousands:
        points_for_getting_thousands =1




    total_found = points_for_getting_units + points_for_getting_tens + points_for_getting_hundrands + points_for_getting_thousands
    print("%s hit , %s miss  "% (total_found , missed - 1))
    if total_found == 4:
        missed -=1 
        print("you managed to guess all the lucky digits : %s " %(lucky_number))



















