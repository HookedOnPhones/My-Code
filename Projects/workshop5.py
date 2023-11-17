import random


def guess_random_number(tries, start, stop):
    target_number = random.randint(start, stop)

    while tries != 0:
        print(f"Number of tries left: {tries}")
        guess = int(input("Guess a number between 0 and 10: "))

        if guess == target_number:
            print("You guessed the correct number!")
            return

        if guess < target_number:
            print("Guess higher!")
        else:
            print("Guess lower!")

        tries -= 1

    print(f"You have failed to guess the number: {target_number}")


# Example usage:
# guess_random_number(5, 0, 10)


def guess_random_num_linear(tries, start, stop):
    target_number = random.randint(start, stop)
    print(f"The number for the program to guess is: {target_number}")

    for attempt in range(1, tries + 1):
        computer_guess = random.randint(start, stop)
        print(f"Number of tries left: {tries}")
        print(f"The program is guessing... {computer_guess}")

        if computer_guess == target_number:
            print("The program guessed the correct number!")
            return

        tries -= 1

    print("The program failed to guess the correct number.")


# Test Driver Code
# guess_random_num_linear(5, 0, 10)


def guess_random_num_binary(tries, start, stop):
    target_number = random.randint(start, stop)
    lower_bound = start
    upper_bound = stop
    print(f"Random number to find: {target_number}")

    while tries > 0:
        guess = (lower_bound + upper_bound) // 2
        if guess == target_number:
            print("Found it!", guess)
            return
        elif guess < target_number:
            lower_bound = guess + 1
            print(f"Guessing higher!")
        else:
            upper_bound = guess - 1
            print(f"Guessing lower!")
        tries -= 1

    print(f"Your program failed to find the number.")


guess_random_num_binary(5, 0, 100)
