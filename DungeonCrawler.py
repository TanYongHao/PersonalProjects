import time 
import random

# Variables
PlayerHealth = 100
EnemyHealth = [50, 100, 150]
EnemyKills = 0
DifficultyChosen = " "
PlayerDamageBuff = 0
PlayerLevel = 1
BlockNegation = 0
Flee = 0

# Difficulties

EnemyDifficulties = {
    "Easy": {
        "EnemyDamage": lambda: random.randint(0, 10),
        "EnemyHealth": EnemyHealth[0],

    },
    "Medium": {
        "EnemyDamage": lambda: random.randint(5, 15),
        "EnemyHealth": EnemyHealth[1],
    },
    "Hard": {
        "EnemyDamage": lambda: random.randint(5, 15),
        "EnemyHealth": EnemyHealth[2],
    }
}

# Introductory Dialogue
Name = input("Enter your name: ")
print("Welcome,", Name + "!" )
time.sleep(1)
print("You currently have slain", EnemyKills, "enemies.")
time.sleep(1)

# Infinite Loop
while True:
    # Deciding Enemy Difficulty Lv1-10
    if PlayerLevel < 10:
        Chance = random.randint(1,3)
        if Chance == 1:
            DifficultyChosen = EnemyDifficulties["Easy"]
            print("You enounter a weak enemy!")
            DifficultyChosen["EnemyHealth"] = 50
            time.sleep(1)
        else:
            DifficultyChosen = EnemyDifficulties["Medium"]
            print("You enounter a moderately strong enemy!")
            DifficultyChosen["EnemyHealth"] = 100
            time.sleep(1)

    # Deciding Enemy Difficulty > Lv10
    if PlayerLevel > 9:
        Chance = random.randint(1,4)
        if Chance == 1:
            DifficultyChosen = EnemyDifficulties["Easy"]
            print("You enounter a weak enemy!")
            DifficultyChosen["EnemyHealth"] = 50
            time.sleep(1)
        elif Chance == 2 or Chance == 3:
            DifficultyChosen = EnemyDifficulties["Medium"]
            print("You enounter a moderately strong enemy!")
            DifficultyChosen["EnemyHealth"] = 100
            time.sleep(1)
        else:
            DifficultyChosen = EnemyDifficulties["Hard"]
            print("You enounter a challenging enemy!")
            DifficultyChosen["EnemyHealth"] = 150
            time.sleep(1)

            # Battle System; Infinite
    while PlayerHealth > 0 and DifficultyChosen["EnemyHealth"]:
        print("You have", PlayerHealth, "health remaining!")
        time.sleep(1)
        print("The enemy has", DifficultyChosen["EnemyHealth"], "health remanining!")
        time.sleep(1)

        # Player Action
        print("Press select an action:")
        print("1. Attack")
        print("2. Block")
        print("3. Flee")
        Action = (input("Awaiting Input: "))
        
        #Player Action Effect
        while Action != str("1") or Action != str("2") or Action != str("3"):
            if Action == str("1"):
                time.sleep(1)
                DamageDealt = DifficultyChosen["EnemyDamage"]() + PlayerLevel
                print("You have dealt", DamageDealt, "damage to the enemy!")
                time.sleep(1)
                DifficultyChosen["EnemyHealth"] -= DamageDealt
                print("The enemy has", DifficultyChosen["EnemyHealth"], "health left!")
                print(" ")
                break
            elif Action == str("2"):
                time.sleep(2)
                BlockNegation = 5 + int(PlayerLevel)
                print("You have decided to block and will defend against the enemy this turn.")
                time.sleep(2)
                break
            elif Action == str("3"):
                time.sleep(2)
                print("You have decided to flee!")
                Flee = random.randint(0, 100)
                if Flee <= 50:
                    DifficultyChosen["EnemyHealth"] = 0
                    break
                else:
                    print("You have failed to flee from the enemy!")
                    break
            else:
                Action = input("Invalid Input. Please try again: ")
            

        # Checking if Enemy is still alive
        if DifficultyChosen["EnemyHealth"] <= 0:
            break
        
        print("The enemy attacks!")
        time.sleep(1)
        DamageDealt = DifficultyChosen["EnemyDamage"]() - PlayerLevel - BlockNegation
        BlockNegation = 0
        if DamageDealt < 0:
            DamageDealt = 0
        else:
            " "
        print("The enemy has dealt", DamageDealt, "damage!")
        time.sleep(1)
        PlayerHealth = PlayerHealth - DamageDealt
        print("You currently have", PlayerHealth, "health remaining.")
        print(" ")
        time.sleep(1)

    if Flee <= 50:
        print("You have successfully fled from the enemy!")
        time.sleep(1)
        print("You continue onwards.")

    if PlayerHealth <= 0 and DifficultyChosen["EnemyHealth"] > 0:
        print("You have been slain!")
        time.sleep(1)
        exit()
    elif PlayerHealth > 0 and DifficultyChosen["EnemyHealth"] <= 0 and Flee > 49:
        print("You have slain the enemy!")
        EnemyKills = EnemyKills + 1
        print("You have slain", EnemyKills, "in total.")
        if EnemyKills % 5 == 0:
            print("You have levelled up!")
            PlayerLevel = PlayerLevel + 1
            print("You are now level", PlayerLevel + ".")
            print("An additional modifier has been placed for your damage.")
        print(input("Press Enter to face another enemy."))
        print(" ")
        time.sleep(2)
    else: 
        print(" ")
        time.sleep(1)



































