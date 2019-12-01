
# input
with open('input.txt') as f:
    data = [int(l.strip()) for l in f]

def calc_fuel(mass):
    if mass <= 0:
        return 0
    return mass + calc_fuel(mass // 3 - 2)

# Part one
print(sum([mass // 3 - 2 for mass in data]))

# Part two
print(sum([calc_fuel(mass) - mass for mass in data]))
