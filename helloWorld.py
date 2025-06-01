counter_right == 0
counter_left == 0

player_name = input("What is your name, Adventurer? ")
print(f"Welcome, {player_name}, to the goblin dungeon!")
while counter_right or counter_left < 3:
    walking_choice = input("Do you want to go left or right? ")


if walking_choice == "left":
    print("You find a treasure chest!")
elif walking_choice == "right":
    print("You find a monster!")


if walking_choice == "right":
    counter_right += 1
else:
    counter_left += 1

if counter_right == 3:
    print("You have died!")
elif counter_left == 3:
    print("You have escaped!")