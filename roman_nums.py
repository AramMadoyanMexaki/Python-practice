def roman_nums_to_arabian(rom_number):
    roman_nums_dict = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }

    number = 0
    prev_value = 0

    for num in reversed(rom_number):
        value = roman_nums_dict[num]

        if value < prev_value:
            number -= value
        else:
            number += value
            prev_value = value

    return number

    # for key, value in roman_nums_dict.items():
    #     if key in rom_number:
    #         if rom_number.count(key) > 1:
    #             number = value * rom_number.count(key)
    #         else:
    #             number += value


print(roman_nums_to_arabian("MI"))
