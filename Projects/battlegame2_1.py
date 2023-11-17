import sys

class Character:
    def __init__(self, name, damage, hp):
        self.name = name
        self.damage = damage
        self.hp = hp

    def display_stats(self):
        print(f"Character: {self.name}")
        print(f"HP: {self.hp}")
        print(f"Damage: {self.damage}\n")

    def set_damage(self, damage):
        self.damage = damage

    def set_hp(self, hp):
        self.hp = hp

    def get_name(self):
        return self.name

def print_choices():
    print("Choose your character")
    characters = {
        "1": "wizard",
        "2": "elf",
        "3": "human",
        "4": "orc",
        "5": "exit"
    }
    for key, value in characters.items():
        print(f"{key}) {value.capitalize()}")

def select_character():
    choice = input("Selection:").lower()
    characters = {
        "1": Character("wizard", 150, 70),
        "wizard": Character("wizard", 150, 70),
        "2": Character("elf", 200, 100),
        "elf": Character("elf", 200, 100),
        "3": Character("human", 20, 150),
        "human": Character("human", 20, 150),
        "4": Character("orc", "1/2 of Dragon's Current HP", 350),
        "orc": Character("orc", "1/2 of Dragon's Current HP", 350),
        "exit": "exit",
        "5": "5"
    }
    if choice in characters:
        if choice == "5" or choice == "exit":
            print("Exiting...")
            sys.exit()
        player_character = characters[choice]
        print(f"You chose {player_character.get_name()}")
        if choice == "orc":
            player_character.display_stats()
        else:
            characters["orc"].display_stats()  # Display Orc stats separately
        return player_character
    else:
        print("Unknown character. Please enter a valid choice.")
        return select_character()

def battle(player_character, dragon):
    while True:
        if player_character.name == "orc" and dragon.hp <= 5:
            player_character.set_damage(5)
            dragon.hp -= player_character.damage
        elif player_character.name == "orc":
            half_dragon_hp = dragon.hp // 2
            player_character.set_damage(half_dragon_hp)
            dragon.hp -= half_dragon_hp
        else:
            dragon.hp -= player_character.damage

        print(f"The {player_character.name} damaged the Dragon!")
        print(f"The Dragon's hitpoints are now: {dragon.hp}\n")

        if dragon.hp <= 0:
            print("You won! The Dragon has lost the battle")
            break

        player_character.hp -= dragon.damage
        print(f"The Dragon damaged the {player_character.name}")
        print(f"The {player_character.name} hitpoints are now: {player_character.hp}\n")

        if player_character.hp <= 0:
            print("You lost!")
            break

def main():
    while True:
        dragon = Character("Dragon", 50, 300)
        print_choices()
        player_character = select_character()
        battle(player_character, dragon)
        print("Play again? Y/N")
        choice = input().lower()
        if choice == "n":
            sys.exit()
        elif choice != "y":
            print("Invalid choice. Please enter 'Y' or 'N'.")

if __name__ == "__main__":
    main()
