counter_right = 0
counter_left = 0

player_name = input("What is your name, Adventurer? ")
print(f"Welcome, {player_name}, to the goblin dungeon!")

def display_status(treasures, monsters):
    print(f"Treasures: {treasures}/3 | Monsters: {monsters}/3")
    print("-" * 40)

def encounter_monster(player_name, monster_name):
    print(f"A wild {monster_name} appears!")
    print(f"{player_name}, runs away screaming for his life!")

while counter_right < 3 and counter_left < 3:
    display_status(counter_left, counter_right)
    walking_choice = input("Do you want to go left or right? ")
    if walking_choice == "left":
        counter_left += 1
        print(f"You have found {counter_left}/3 treasure chests")
    elif walking_choice == "right":
        counter_right += 1
        print(f"You have found {counter_right}/3 monsters")
        encounter_monster(player_name, "goblin")

# After the loop ends...
print(f"You have found {counter_left}/3 treasure chests and {counter_right}/3 monsters.")

if counter_right == 3:
    print("You have died!")
elif counter_left == 3:
    print("You have escaped!")