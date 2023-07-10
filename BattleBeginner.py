import random
import time

# Health Variables, only Enemy Health changes depending on difficulty
PlayerHealth = 100
EnemyHealth = [50, 100, 150, 500]

# Writing Down Difficulties
ValidDifficulties = ["left", "middle", "right",]

# StarterWeapon Function | Dictionary Styled

StarterWeapon = {
    "left": {
        "StarterWeapon": lambda: random.randint(0, 10),
        "EnemyHealth": EnemyHealth[0]
    },
    "middle": {
        "StarterWeapon": lambda: random.randint(5, 15),
        "EnemyHealth": EnemyHealth[1] 
    },
    "right": {
        "StarterWeapon": lambda: random.randint(10, 20),
        "EnemyHealth": EnemyHealth[2]
    },
    "boss": {
        "GreatWeapon": lambda: random.randint(100, 200),
        "EnemyWeapon": lambda: random.randint(10,20),
        "EnemyHealth": EnemyHealth[3]
    }
}

# Introductory Dialogue
print("Welcome to the Adventure Game!")
time.sleep(1)
print("As a new explorer, you have decided to tackle the Lost City. An ambitious first start, but a rewarding one.")
time.sleep(2)
print("After spending some hours exploring and eliminating ghouls and skeletons alike, you arrive in front of the City's castle. A marvel to behold, as tall as the spires you've seen back home.")
time.sleep(4)
print("Snapping out of your enchantment, you enter the castle.")
time.sleep(1)
print("As you do so, however, the castle entrance slams behind you, with no way out.")
time.sleep(2)
print("In front of you lies three doors, leading to unknown rooms behind.")
print(" ")
time.sleep(2)

while True:
    # Player selects Room
    print("Which room do you enter?:")
    print("Left")
    print("Middle")
    print("Right")
    Difficulty = input("Please select: ")

    # Detects invalid input
    while Difficulty.lower() not in ValidDifficulties:
        print("This is an invalid input. Please retry again.")
        Difficulty = input("Awaiting Input: ")

    # Detects and Utilises Respective Difficulty Code
    DifficultyVerification = StarterWeapon[Difficulty.lower()]

    # Random Chance Event | Decreases Health Slightly if Failed
    print("As you carefully open the", Difficulty.lower(), "door, you are suddenly attacked by an unknown enemy!")
    time.sleep(2)
    Dodge = random.randint(0,2)
    if Dodge <= 1:
        print("You are able to closely evade the enemy, saving yourself from being injured before battle.")
    else:
        print("Being unable to dodge the swift attack, you are able to redirect the attack towards your chest, injuring yourself but not weaking your fighting capabilities in the slightest.")
        PlayerHealth = PlayerHealth - 5
    
    # More Dialogue 
    time.sleep(3)
    print("Looking closely, you recognise the enemy to be a Higher Ghoul, a fairly rare enemy and an evolved form of those ghouls you fought earlier.")
    time.sleep(3)
    print("Being able to recognise it, you can tell it has", DifficultyVerification["EnemyHealth"], "health.")
    time.sleep(2)
    print("Without giving it time to attack again, you decide to immediately spring into action and attack it first.")
    time.sleep(2)
    print(" ")


    while PlayerHealth > 0 and DifficultyVerification["EnemyHealth"] > 0:
        
        # Player Attacking
        print(input("Press Enter to Attack: "))
        time.sleep(1)
        damage = DifficultyVerification["StarterWeapon"]()
        print("You have dealt", damage, "damage!")
        DifficultyVerification["EnemyHealth"] -= damage
        print("The enemy is now left with", DifficultyVerification["EnemyHealth"], "health!")

        # Checking if Enemy is Defeated
        if DifficultyVerification["EnemyHealth"] <= 0:
            break

        # Enemy Attacking
        print(" ")
        print("The enemy attacks!")
        time.sleep(2)
        damage = DifficultyVerification["StarterWeapon"]()
        print("The enemy has dealt", damage, "damage!")
        PlayerHealth = PlayerHealth - damage
        print(" ")
        print("You are now left with", PlayerHealth, "health.")

    print(" ")

    # Victory Statements
    if PlayerHealth <= 0 and DifficultyVerification["EnemyHealth"] > 0:
        print("You have failed to defeat the enemy and have died.")
        Retry = input("Would you like to try again? (Yes/No): ")
    else:
        break

    # Retry Statement
    if Retry.lower() == "yes":
        PlayerHealth = 100
        DifficultyVerification["EnemyHealth"] = EnemyHealth[ValidDifficulties.index(Difficulty.lower())]
    else: 
        print("Thank you for playing!")
        exit()

print("As you slit the throat of the Higher Ghoul in a swift cut, the monster crumbles and dissipates into ashes. Standard.")
time.sleep(3)

# First Decision | Results in Potential Health Boost
print("What do you do now?")
print("1. Look Around")
print("2. Proceed Onwards")
Decision1 = input(str("Input the number of your decision: "))
while True:
    if Decision1 == "1":
        print(" ")
        print("You decide to look around the room before proceeding.")
        print("The room appears to be some sort of dining room, furbished fantastically but not enough to be seen as something a royal would use. Accomdated for the King or Queen's many guests, mayhaps.")
        time.sleep(5)
        print("Sunlight illuminates the whole room, coming through the giant windows on both sides of the room, outfitted with a small countertop near the bottom.")
        time.sleep(3)
        print("As you scan the room for anything more interesting, you see a ring sitting on left countertop near the windows.")
        time.sleep(2)
        print("Examining the ring, it looks to be your standard ring, paired perfectly with an Emarald near the top.")
        time.sleep(2)
        print("Putting the ring on your index finger, you instantly feel reguvenated and filled back with health. Guess looking around was a good idea.")
        PlayerHealth = PlayerHealth + 50
        print("Your health is now", str(PlayerHealth) + "!")
        time.sleep(3)
        break
    elif Decision1 == "2":
        print(" ")
        print("You decide to continue onwards without looking around, determined to leave as soon as possible.")
        break
    else:
        print(str("Invalid input. Please try again."))
        Decision1 = input("Please input a number: ")


# Consequence of Decision | Pivotal to Win
print(" ")
if Difficulty.lower() == "middle" or Difficulty.lower() == "right":
    print("As you carefully open the second door, you're greeted by what seems to be an armoury.")
    time.sleep(2)
    print("The room seems entirely ransacked, with the exception of a glowing sword in the middle of the room.")
    time.sleep(2)
    print("As you head near the middle of the room, the sword glows brighter and brighter, reaching its brightest whilst you stand beside it.")
    time.sleep(3)
    print("Pulling out the sword, the sword feels warm to the touch, yet familiar.")
    time.sleep(2)
    print("Equipped with your newer and stronger sword, you head onwards further.")
    time.sleep(2)
    print("Your damage has increased by 1000%!")
    time.sleep(1)
else:
    print("You carefully head into the next room, being greeted by what appears to be a fully ransacked armoury.")
    time.sleep(2)
    print("A shame, as you've have been able to upgrade your weapon here if there was anything good.")
    time.sleep(2)
    print("As you leave, you wonder who was able to take all the weaponry here before they left. Maybe it past adventurers. Maybe it was guards who fled just before the City fell.")
    time.sleep(4)

print(" ")

# Dialogue 
print("As you press onwards, you go through room after room, being met by either complete emptiness or the occassional loot left behind.")
time.sleep(2)
print("Your health has increased by 50!")
time.sleep(1)
PlayerHealth = PlayerHealth + 50
print(" ")
print("Finally, after what feels like hours, you reach the outside of the final room. The throne room.")
time.sleep(2)
print("After some checks on your armour, you carefully enter push open the doors to the room, and enter.")
time.sleep(2)
print("Entering the room, you're instantly greeted by a pungent smell. Looking around, you see pools of blood staining the floors, both dried and still wet.")
time.sleep(3)
print("As you turn your eyes towards the throne, you spot a robed skeleton sitting on it, wielding a scepter. A Lich. And a pretty strong one as well.")
time.sleep(3)
print("Same as before, you instantly jump into action, beginning the long and cruel fight with the final boss of the Castle.")
time.sleep(3)

# Configuring Difficulty
DifficultyVerification = StarterWeapon["boss"]

print("You current health is", str(PlayerHealth) + ".")
print("The enemy's health is", str(DifficultyVerification["EnemyHealth"]) + ".")

while PlayerHealth > 0 and DifficultyVerification["EnemyHealth"] > 0:
        
     # Player Attacking
    print(input("Press Enter to Attack: "))
    time.sleep(1)
    damage = DifficultyVerification["GreatWeapon"]()
    print("You have dealt", damage, "damage!")
    DifficultyVerification["EnemyHealth"] -= damage
    print("The enemy is now left with", DifficultyVerification["EnemyHealth"], "health!")

    # Checking if Enemy is Defeated
    if DifficultyVerification["EnemyHealth"] <= 0:
        break

    # Enemy Attacking
    print(" ")
    print("The enemy attacks!")
    time.sleep(2)
    damage = DifficultyVerification["EnemyWeapon"]()
    print("The enemy has dealt", damage, "damage!")
    PlayerHealth = PlayerHealth - damage
    print(" ")
    print("You are now left with", PlayerHealth, "health.")


# Second Victory Statements
if PlayerHealth <= 0 and DifficultyVerification["EnemyHealth"] > 0:
    print("You have failed to defeat the enemy and have died.")
    Retry = input("Would you like to try again? (Yes/No): ")
    

# Retry Statement
    if Retry.lower() == "yes":
        PlayerHealth = 100
        DifficultyVerification["EnemyHealth"] = EnemyHealth[ValidDifficulties.index(Difficulty.lower())]
    else: 
        print("Thank you for playing!")
        exit()

# Victory Statement
print("As you plunge your sword into the Lich's chest, it lets out a blood-curdling scream and crumbles into a pile of ashes.")
time.sleep(2)
print("You win!")

# Final Statement
print("Thank you for playing!")
exit()
