# * * * x x x x t t t t t t

def calculate():
    iterations, day_num = (int(x) for x in input().split())
    consumed = 0
    ava_bales = 0

    for i in range(iterations):
        curr_day, new_bales = (int(x) for x in input().split())
        ava_bales += new_bales

        for i in range(ava_bales):
            consumed += 1
            curr_day += 1
            if curr_day > day_num:
                break
        if curr_day > day_num:
            break

    print(consumed)

calculate()