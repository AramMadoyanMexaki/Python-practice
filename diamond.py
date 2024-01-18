def give_diamond(n):
    # If the number is negative or even, return None
    if n < 0 or n % 2 == 0:
        return None

    # This is the text that will then look like a diamond
    diamond = ""
    # This is the number of spaces per line. The number of spaces changes in a cycle to maintain symmetry.
    spaces = n // 2
    # Number of initial asterisks
    stars = 1


    for i in range(n):
        diamond += " " * spaces + "*" * stars + "\n"
        if i < n // 2:
            spaces -= 1
            stars += 2
        else:
            spaces += 1
            stars -= 2

    return diamond

print(give_diamond(5))
