import random


def field_of_wonders(words):
    random_word = random.choice(words).lower()
    attempt = len(random_word)

    secret_chars = attempt * "_"

    letters_blocks = []
    user_word = []

    tmp_updates_blocks = []
    tmp_list_random_word = []

    for char in secret_chars:
        letters_blocks.append(char)

    while attempt > 0:
        user_attempt = str(input("Try to guess one of the letters of the word. "))

        user_word.append(user_attempt)

        repeated_letter = 0

        for letter in random_word:
            tmp_list_random_word.append(letter)

            if random_word.count(letter) >= 2:
                repeated_letter += 1

        if user_attempt in tmp_list_random_word:
            letter_idx = random_word.find(user_attempt)

            letters_blocks[letter_idx] = user_attempt

            tmp_updates_blocks = "".join(letters_blocks)

            print(tmp_updates_blocks)

            # if user_word.index(user_attempt) == random_word.find(user_attempt):
            #     print("You guessed the word, congratulations!")

            if "_" not in letters_blocks:
                return "You guessed the word, congratulations!"

        else:
            print(f"The letter '{user_attempt}' is not in the saved word. Try again!")

        attempt -= 1

        if attempt == 0:
            return f"You couldn't guess the secret word and that word was {random_word}."

    return tmp_updates_blocks


print(field_of_wonders(["Hello", "Armenia", "Python"]))
