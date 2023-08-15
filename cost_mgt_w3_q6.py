

units = [3400, 3303, 3192, 3500 ]
for unit in units:
    profit = (unit * 450) - (unit * 225) - 125000
    profit = profit - (.45 * profit)
    print(unit, " ", profit)