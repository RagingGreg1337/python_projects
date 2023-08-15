import sys
player_name = {}

num = 1
while True:
    try: 
        num_of_players = int(input("Hello DM! How many players will you be having today? "))
        break
    except ValueError:
        print("Invalid answer! Please enter a number. ")


while num_of_players >= num:
    if num_of_players >= 6:
        print("Sorry! that's too many players!")
        break
    else:
        while True:
            try:   
                names = input("what is player" + str(num) + " name: ")
                break
            except ValueError:
                print("Invalid name! Please input a valid name")
        while True:
            try:
                turn =  int(input("What was " + names + " initiative "))
                break
            except ValueError:
                print("Invaild number! Please try again.")
    player_name[names]=turn 
    num += 1   

print(player_name)