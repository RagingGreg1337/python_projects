player_name = []

num = 1
num_of_players = int(input("Hello DM! How many players will you be having today?"))

while num_of_players >= num:
    if num_of_players >= 7:
        print("Sorry! that's too many players!")
        break
    else:   
        names = input("what is player" + str(num) + " name: ")
        player_name.append(names)
    num += 1
    print(player_name[:4])