def encode(str):
    vowels = "aeiou"
    coded_word = ""

    for char in str:
        if char in vowels:
            if char == 'a':
                coded_word += '1'
            elif char == 'e':
                coded_word += '2'
            elif char == 'i':
                coded_word += '3'
            elif char == 'o':
                coded_word += '4'
            elif char == 'u':
                coded_word += '5'
        else:
            coded_word += char

    return coded_word

def decode(str):
    vowel_nums = "12345"
    decoded_text = ""

    for char in str:
        if char in vowel_nums:
            if char == '1':
                decoded_text += 'a'
            elif char == '2':
                decoded_text += 'e'
            elif char == '3':
                decoded_text += 'i'
            elif char == '4':
                decoded_text += 'o'
            elif char == '5':
                decoded_text += 'u'
        else:
            decoded_text += char

    return decoded_text

print(encode("This is an encoding test."))
print(decode("Th3s 3s 1n 2nc4d3ng t2st."))
