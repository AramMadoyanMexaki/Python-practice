text = input("Enter a text: ")

def pig_latin(text):
    text = text.split(" ")
    
    pig_latin_str = ""
    
    for word in text:
        for char in word:
            if not char.islower() and not char.isupper():
                return pig_latin_str + char
        else:
            pig_latin_str += word[1:] + word[0] + "ay "

    return pig_latin_str
    
print(pig_latin(text))



