from collections import Counter

input0, input1 = 372304, 847060


def password_counter(in0, in1):
    passwords1, passwords2 = 0, 0
    for num in range(in0, in1):
        num = str(num)
        if list(sorted(num)) == list(num):
            if len(list(set(num))) != len(list(num)):
                passwords1 = passwords1 + 1

                if 2 in Counter(num).values():
                    passwords2 = passwords2 + 1

    return passwords1, passwords2


# Part 1 / part2
print(password_counter(input0, input1))
