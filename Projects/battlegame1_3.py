import sys

class Character:
    def __init__ (self, my_name, my_damage, my_hp):
        self.my_name = my_name
        self.my_damage = my_damage
        self.my_hp = my_hp
    def stat_display(self):
        print("Character:", self.my_name)
        print("HP:", self.my_hp)
        print("Damage:", self.my_damage, "\n")
    def change_damage(self, my_damage):
        self.my_damage = my_damage
    def change_hp(self, my_hp):
        self.my_hp = my_hp
    def get_name (self):
        return self.my_name

# Prompt for characters
def print_choices():    
    print("Choose your character")
    print("1) wizard")
    print("2) elf")
    print("3) human")
    print("4) orc")
    print("5) Exit")

# Prompted for selection
def play():
    choice = input("Selection:").lower()
    if choice == "1" or choice == "wizard":
        playercharacter = Character("wizard", 150, 70)
        print("You chose", str(playercharacter.get_name()))
        playercharacter.stat_display()

    elif choice == "2" or choice == "elf":
        playercharacter = Character("elf", 200, 100)
        print("You chose", str(playercharacter.get_name()))
        playercharacter.stat_display()

    elif choice == "3" or choice == "human":
        playercharacter = Character("human", 20, 150)
        print("You chose", str(playercharacter.get_name()))
        playercharacter.stat_display()

    elif choice == "4" or choice == "orc":
        playercharacter = Character("orc", "1/2 of Dragon's Current HP", 350)
        print("You chose", str(playercharacter.get_name()))
        playercharacter.stat_display()

    elif choice == "5" or choice == "exit":
        print("Exiting...")
        sys.exit()

    else:
        print("Unknown character. Please enter a valid choice.")
        play()
    return playercharacter

def battle(playercharacter, dragon):
    while True:
        if playercharacter.my_name == "orc" and dragon.my_hp <= 5:  # when dragon's hp is less than or equal to 5
            playercharacter.change_damage(5)  # change orc's damage to being 5
            dragon.my_hp -= playercharacter.my_damage

        elif playercharacter.my_name == "orc":
            half_dragon_hp = dragon.my_hp // 2  # Calculate half of Dragon's HP
            playercharacter.change_damage(half_dragon_hp)  # Orc deals half of Dragon's HP as damage
            dragon.my_hp -= half_dragon_hp  # Update Dragon's HP
        
        else:
            dragon.my_hp -= playercharacter.my_damage

        print("The", playercharacter.my_name, "damaged the Dragon!")
        print("The Dragon's hitpoints are now:", dragon.my_hp, "\n")

        if dragon.my_hp <= 0:
            print("You won! The Dragon has lost the battle")
            break

        print("The Dragon damaged the", playercharacter.my_name)
        playercharacter.my_hp -= dragon.my_damage  # Dragon damages the player character
        print("The", playercharacter.my_name, "hitpoints are now:", playercharacter.my_hp, "\n")

        if playercharacter.my_hp <= 0:
            print("You lost!")
            break

while True:
    dragon = Character("Dragon", 50, 300)
    print_choices()
    playercharacter = play()
    battle(playercharacter, dragon)
    print("Play again? Y/N")
    choice = input().lower()
    if choice == "y":
        print("Good Luck!")
    elif choice == "n":
        sys.exit()
    else:
        print("Invalid choice. Please enter 'Y' or 'N'.")
