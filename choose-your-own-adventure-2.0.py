name = "Sqiddyinkster🤣"
print(f"Welcome to {name}'s choose ur own adventure game! Let's get started.")
print("You find yourself in a dark, dank room with 2 doors. One is red and one is blue.")
door_choice = input("Which door do you go in? Type 'red' for the red door or 'blue' for the blue door: ")

if door_choice == "red":
    print("You walk into the red door and meet a mad scientist who's on a mission to rule the village he lives in!")
    choice_1 = input("Do you want to help? Type '1' for help or '2' for don't help: ")
    
    if choice_1 == "1":
        print("You help him achieve village domination! In return, he offers you one of the following two items: an instant money machine or an infinite food pot.")
        choice_3 = input("Do you take the money machine, the food pot, or both? Type 'm' for the money machine, 'p' for the food pot, or 'b' to take both: ")

        if choice_3 == "m":
            print("You got an instant money making machine! You print yourself $500,000 and see a Lamborghini and a helicopter for sale.")
            mini_choice = input("Which do you buy? Type 'l' for the Lambo or 'h' for the helicopter: ")
            
            if mini_choice == "l":
                print("""__________GAME OVER__________
You now own a Lambo! You decide to take her for a spin in rush hour. You speed down the highway at 84.68 kmph and crash into a truck carrying loads of gunpowder. The gunpowder explodes, taking you and your Lambo with it.""")
            elif mini_choice == "h":
                print("""__________SUCCESS__________
You fly your new helicopter to your house and live happily ever after.""")
        
        elif choice_3 == "p":
            print("You take the pot and accidentally make enough food to last you 6 years.")
            mini_choice1 = input("Do you sell the food or eat it? Type 'sell' to sell it or 'eat' to eat it: ")
            
            if mini_choice1 == "sell":
                print("""__________GAME OVER__________
You try to sell it all in one day. You're becoming somewhat rich, but you forget to feed yourself. You realize this too late, and die of hunger.""")
            else:
                print("""__________GAME OVER__________
You get the silly idea of eating it all in one sitting. When you swallow your 60th burger, you blow up and die.""")
        
        elif choice_3 == "b":
            print("""__________GAME OVER__________
You snatch both and try to run before the scientist notices. But he reacts quickly, activating emergency lockdown mode. You try to escape through a window, but lasers chop you to bits!""")
        else:
            print("Invalid choice.")
    
    else:
        print("""__________GAME OVER__________
You say no, and the scientist grabs a laser gun and vaporizes you.""")
    
elif door_choice == "blue":
    print("You walk into the blue door and find a turtle who asks you to eat a fish.")
    choice_2 = input("Do you eat the fish? Type '1' for yes or '2' for no: ")

    if choice_2 == "1":
        print("The turtle thanks you and gives you a magical shell that can grant one wish.")
        choice_4 = input("What's your wish? Type '$' for infinite money or 'home' to go home: ")
        
        if choice_4 == "home":
            print("""__________SUCCESS__________
The shell whisks you back home and you live happily ever after with no worries in the world.""")
        elif choice_4 == "$":
            print("""__________GAME OVER__________
You get your money, but it's from 1,000,000,000 years in the future. It's worthless. You starve to death.""")
        else:
            print("Invalid choice.")
    else:
        print("""__________GAME OVER__________
The turtle becomes angry and throws you out of the room.""")
else:
    print("Invalid choice. Please select either 'red' or 'blue'.")
