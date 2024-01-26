class Numbers():
    def __init__(self):
        self.one = "one"
        self.two = "two"
        self.three = "three"
        self.four = "four"
        self.five = "five"
        self.six = "six"
        self.seven = "seven"
        self.eight = "eight"
        self.nine = "nine"
        self.zero = "zero"

    def number_to_text(self, number):
        number = str(number)
        number_text = ""

        for char in number:
            char = int(char)

            if char == 0:
                number_text += self.zero
            elif char == 1:
                number_text += self.one
            elif char == 2:
                number_text += self.two
            elif char == 3:
                number_text += self.three
            elif char == 4:
                number_text += self.four
            elif char == 5:
                number_text += self.five
            elif char == 6:
                number_text += self.six
            elif char == 7:
                number_text += self.seven
            elif char == 8:
                number_text += self.eight
            elif char == 9:
                number_text += self.nine
            else:
                print("Invalid value")

        return number_text

numbers_object = Numbers()
print(numbers_object.number_to_text(1984))


