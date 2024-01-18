def high(x):
    # Variable to store the word with the highest sum
    highest_word = ""

    alphabet = {
        'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10,
        'k': 11, 'l': 12, 'm': 13, 'n': 14, 'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19,
        't': 20, 'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25, 'z': 26
    }

    # Let's turn the sentence word by word into an array
    words = x.split(' ')

    # Variable to store the highest sum found so far

    highest_sum = 0

    for word in words:
        # Let's turn each word of the sentence into a lowercase letter.
        word = word.lower()

        # Variable to calculate the sum for each word
        current_sum = 0

        for char in word:
            current_sum += alphabet.get(char, 0) # Sum the positions of characters in the word

            if current_sum > highest_sum: # Update the highest sum
                highest_sum = current_sum # Set the current word as the word with the highest sum
                highest_word = word

    return highest_word


print(high("Hello man, how do you do guys ?"))
