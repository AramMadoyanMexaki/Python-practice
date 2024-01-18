# Run-length encoding (RLE)

# RLE-ն տվյալների անկորուստ սեղմման շատ պարզ ձև է, որում տվյալների գործարկումները պահվում են որպես մեկ տվյալների արժեք և հաշվարկ:

# RLE-ի պարզ ձևը կկոդավորի «AAABBBCCCD» տողը որպես «3A3B3C1D», ինչը նշանակում է, որ սկզբում կա 3 A, ապա 3 B, ապա 3 C և վերջում կա 1 D:

# Ձեր խնդիրն է գրել RLE կոդավորիչ և ապակոդավորիչ՝ օգտագործելով այս տեխնիկան: Կոդավորվող տեքստերը միշտ բաղկացած կլինեն միայն մեծատառ նիշերից, առանց թվերի:

def encode_rle(data):
    encoded = ""
    count = 0
    
    for i in range(len(data)):
        count += 1
        if i == len(data) - 1 or data[i] != data[i + 1]:
            encoded += f"{count}{data[i]}"
            count = 0
            
    return encoded

def decode_rle(data):
    decoded = ""
    count = ""
    
    for i in data:
        if i.isdigit():
            count += i
        else:
            decoded += i * int(count)
            count = ""
            
    return decoded
 
print(encode_rle("CCCOONNPDVVW")) # 3C2O2N1P1D2V1W
print(decode_rle("3C2O2N1P1D2V1W")) # CCCOONNPDVVW
