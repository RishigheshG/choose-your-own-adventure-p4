name = input("What do we call you? ")
print("Welcome to the adventure,", name + "!")

answer = input("You find yourself at a crossroads. Do you want to go left or right? (left/right) ").lower()

if answer == "left":
    answer = input("You encounter a wild river. Do you want to swim across or build a raft? (swim/raft) ").lower()
    if answer == "swim":
        print("You bravely swim across the river but get swept away by the current. Game over!")
    elif answer == "raft":
        print("You successfully build a raft and cross the river safely. You win!")
    else:
        print("Invalid choice. Game over!")
elif answer == "right":
    answer = input("You come across a dark forest. Do you want to enter or go around it? (enter/around) ").lower()
    if answer == "enter":
        print("You get lost in the forest and can't find your way out. Game over!")
    elif answer == "around":
        print("You wisely go around the forest and reach your destination safely. You win!")
    else:
        print("Invalid choice. Game over!")
else:
    print("Invalid choice. Game over!")