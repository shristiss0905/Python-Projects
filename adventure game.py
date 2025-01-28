# Introduction to the game
print("Welcome to The Space Odyssey!")
name = input("What is your name, Captain? ")

print(f"\nCaptain {name}, your ship 'Starlight' has crash-landed on the mysterious planet Xyphos.")
print("You are now stranded, and it's up to you to explore the unknown surface.")
first_choice = input("Do you want to explore the crash site or venture into the alien ruins? (crash/ruins) ").lower()

if first_choice == "crash":
    print("\nYou decide to explore the crash site first. The wreckage is scattered around, and your ship's systems are offline.")
    print("Suddenly, you hear a low hum from the wreckage and notice a strange glowing artifact.")
    artifact = input("Do you want to touch the glowing artifact or leave it alone? (touch/leave) ").lower()

    if artifact == "touch":
        print("\nYou touch the artifact, and a strange energy pulses through your body.")
        print("Suddenly, a **teleportation beam** activates, and you are transported to another dimension!")
        print("You find yourself on an alien ship, surrounded by unknown beings.")
        print("A figure approaches you, offering a choice: join them or return to your crashed ship.")
        dimension_choice = input("Do you join them or return to the crash site? (join/return) ").lower()

        if dimension_choice == "join":
            print(f"\nCaptain {name}, you've joined the alien beings and explored the galaxy with them, gaining vast knowledge and power.")
            print("You've become a legendary space traveler, known across the universe!")
            print("You WIN!")
        elif dimension_choice == "return":
            print(f"\nCaptain {name}, you decide to return to your ship, but the teleporter malfunctions and you are trapped in another dimension.")
            print("You have failed to escape... but your story continues in another universe.")
            print("Game Over.")
        else:
            print("That is not a valid choice. The alien beings vanish, and you are left stranded.")
            print("Game Over.")

    elif artifact == "leave":
        print("\nYou decide to leave the artifact alone and head toward the alien ruins.")
        print("As you walk, you find a **hidden door** beneath some rocks, leading you into a **dark underground tunnel**.")
        print("The tunnel leads to a massive alien city, full of strange technology.")
        city_choice = input("Do you explore the city or try to find a way back to your ship? (explore/ship) ").lower()

        if city_choice == "explore":
            print(f"\nCaptain {name}, you explore the alien city and discover an advanced machine that can repair your ship!")
            print("You fix your ship and continue your journey across the galaxy!")
            print("You WIN!")
        elif city_choice == "ship":
            print(f"\nCaptain {name}, you decide to return to your ship, but an alien creature attacks you on the way back!")
            print("You have been defeated by the alien creature.")
            print("Game Over.")
        else:
            print("That is not a valid choice. You are stuck in the tunnel, and your journey ends here.")
            print("Game Over.")

elif first_choice == "ruins":
    print("\nYou decide to explore the alien ruins first. The ruins are ancient, with strange markings on the walls.")
    print("You discover a **secret chamber** beneath the ruins, filled with alien artifacts and a strange glowing orb.")
    orb_choice = input("Do you touch the orb or examine the chamber further? (touch/examine) ").lower()

    if orb_choice == "touch":
        print("\nYou touch the orb, and it glows brightly, activating a hidden system that opens a portal.")
        print("The portal transports you to the surface of another planet, **Zorath**, where a battle is taking place.")
        battle_choice = input("Do you join the battle to fight for the planet or escape through the portal? (fight/escape) ").lower()

        if battle_choice == "fight":
            print(f"\nCaptain {name}, you fight bravely and help the Zorathians defeat the invaders.")
            print("You are hailed as a hero and gain the trust of the alien planet!")
            print("You WIN!")
        elif battle_choice == "escape":
            print(f"\nCaptain {name}, you escape back to Xyphos, but the portal closes before you can make it back to your ship.")
            print("You are stuck on the alien planet, lost in space.")
            print("Game Over.")
        else:
            print("That is not a valid choice. The portal shuts down, and you are trapped in the dimension.")
            print("Game Over.")
    
    elif orb_choice == "examine":
        print("\nYou examine the chamber further and discover a hidden passage leading deep into the ruins.")
        print("The passage leads to an ancient **alien artifact** that could change the course of space history!")
        print(f"\nCaptain {name}, you’ve unlocked a powerful weapon, but your ship is still broken.")
        print("You must find a way to escape the planet or explore more of the galaxy.")
        print("Game Over... for now.")

else:
    print("That is not a valid choice. Your story ends here.")
    print("Game Over.")

print("Good Day!")
