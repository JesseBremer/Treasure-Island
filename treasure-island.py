print("Welcome to Treasure Island! \n"
      "Your mission is to find the treasure, matey.")

character_movement = input("As you land on the beach, before you are two paths into the forested island. \n"
                           "Which direction do you take? Type 'left' or 'right' \n")

if character_movement == "left":
    character_movement = input(
        "You travel down the forested path and come across a cave. Do you dare enter inside? \n"
        "Type 'enter' to go inside or 'continue' to keep traveling the pathway. \n")
    if character_movement == "enter":
        character_movement = input("You decide to be bold and enter the cave. \n"
                                   "Inside the cave you see torches ahead. \n"
                                   "You've come this far so why not continue? \n"
                                   "You reach the end of the cave where you find three different coloured doors. \n"
                                   "Which one will you choose? 'red', 'yellow', or 'blue' ? \n")
        if  character_movement == "red":
            print(
                "You open the red door and... \n"
                "Congratulations, you found the treasure! \n"
                "You flee the island with all your riches!")
        elif character_movement == "blue":
            print("You open the blue door and... \n"
                  "Immediately you are shot through the chest by an arrow trap. \n"
                  "Game Over!")
        elif character_movement == "yellow":
            print(
                "You open the yellow door and... \n"
                "As you step through - the door slams behind you! \n"
                "You find yourself trapped inside with other an array of bones scattered across the floor. \n"
                "You're not getting out of here. Game over!")
    else:
        print("You continue down the path but get caught in net trap a few paces away from the cave! \n"
              "Cannibals from the island have caught their dinner unfortunately for you... \n"
              "Game over!")

else:

    print("You fell into a hole and starved to death. \n"
          "Game over!")

