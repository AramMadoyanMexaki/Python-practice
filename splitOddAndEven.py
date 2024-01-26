def splitOddAndEven(number):
    oddNumber = ""
    evenNumber = ""
    zero = ""

    for char in str(number):
        char = int(char)

        if char == 0:
            zero += str(char)
        elif char % 2 == 0:
            evenNumber += str(char)
        else:
            oddNumber += str(char)

    oddNumber = int(oddNumber)
    evenNumber = int(evenNumber)

    array = [oddNumber, evenNumber]

    # if number % 2 != 0 or number % 2 == 0:
    #     return number

    return array

print(splitOddAndEven(9870))
