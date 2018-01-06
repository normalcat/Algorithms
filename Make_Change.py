def change(cents):
    coins = {}
    while cents > 0:
        if cents >= 100:
            coins['dollars'] = cents/100
            cents = cents % 100
        elif cents >= 25:
            coins['quarters'] = cents/25
            cents = cents % 25
        elif cents >= 10:
            coins['dimes'] = cents/10
            cents = cents % 10
        elif cents >= 5:
            coins['nickels'] = cents/5
            cents = cents % 5
        elif  cents >= 1:
            coins['pennies'] = cents/1
            cents = cents % 1
    return coins

print change(572)
