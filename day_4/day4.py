input0, input1 = '372304', '847060'
passwords = 0

for num in range(int(input0), int(input1)):
    num = str(num)
    if list(sorted(num)) == list(num):
        if len(list(set(num))) != len(list(num)):
            passwords = passwords + 1

# Part 1
print(passwords)
