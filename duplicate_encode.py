def duplicate_encode(word):
    # This is the text in which we will put the coded version of the "word" variable.
    coded_text = ""
    # Convert all letters of the "word" function argument to lowercase so that it doesn't matter if any letter is uppercase or lowercase.
    word = word.lower()

    for i in range(len(word)):
        #Let's check whether there is a letter in the word that is repeated more than 1 time, using the count() method.
        if word.count(word[i]) > 1:
            coded_text += ")"
        else:
            coded_text += "("

    return coded_text

print(duplicate_encode("Success"))
