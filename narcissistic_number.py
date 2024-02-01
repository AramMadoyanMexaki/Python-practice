# Նարցիսիստական թիվը (կամ Արմսթրոնգի թիվը) դրական թիվ է, որն իրենից ներկայացնում է իր սեփական թվանշանների գումարը, որոնցից յուրաքանչյուրը բարձրացված է տվյալ բազայի թվանշանների քանակին:
# 1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153

# 1652 (4 նիշ), որը Նարցիսիստական չէ.
# 1^4 + 6^4 + 5^4 + 2^4 = 1 + 1296 + 625 + 16 = 1938.

def narcissistic(value):
    value = str(value)
    digit_sum = 0

    for digit in value:
        digit = int(digit)
        number_digits = digit ** len(value)
        digit_sum += number_digits

    value = int(value)

    if digit_sum == value:
        return True
    else:
        return False

print(narcissistic(153))