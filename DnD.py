player_name = {}

num = 1
num_of_players = int(input("Hello DM! How many players will you be having today? "))

while num_of_players >= num:
    if num_of_players >= 7:
        print("Sorry! that's too many players!")
        break
    else:   
        names = input("what is player" + str(num) + " name: ")
        turn =  int(input("What was " + names + " initiative "))
        player_name[names]=turn 
    num += 1   

print(player_name)