# Գրեք մի ֆունկցիա, որը վերցնում է մեկ կամ մի քանի բառերից բաղկացած տողը և վերադարձնում է նույն տողը, բայց բոլոր հինգ կամ ավելի տառային բառերով հակադարձված են (Ինչպես այս Kata-ի անունը): Մուտքագրված տողերը բաղկացած կլինեն միայն տառերից և բացատներից: Բացատները կներառվեն միայն մեկից ավելի բառերի առկայության դեպքում:

# 1-ին եղանակ

def spin_words(sentence):
    result = ""
    char = len(sentence) - 1

    if len(sentence) >= 5:
        while char >= 0:
            result += sentence[char]

            char -= 1
    else:
        return sentence
    
    return result

print(spin_words("Hey wollef sroirraw")) 

# 2-րդ եղանակ

def spin_words2(sentence):
    words = sentence.split()

    for i2 in range(len(words)):
        if len(words[i2]) >= 5:
            words[i2] = words[i2][::-1]
        
    result = " ".join(words)

    return result

print(spin_words2("Hey wollef sroirraw"))