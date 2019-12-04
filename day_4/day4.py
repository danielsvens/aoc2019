from collections import Counter

input0, input1 = '372304', '847060'


def password_counter(in0, in1):
    passwords1, passwords2 = 0, 0
    for num in range(int(in0), int(in1)):
        num = str(num)
        if list(sorted(num)) == list(num):
            if len(list(set(num))) != len(list(num)):
                passwords1 = passwords1 + 1

                c = Counter(num)
                if any([(k, v) for k, v in [(k, v) for k, v in c.items() if v > 1] if v == 2]):
                    passwords2 = passwords2 + 1

    return passwords1, passwords2


# Part 1 / part2
print(password_counter(input0, input1))


