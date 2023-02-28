def calculate():
    iterations, day_num = (int(x) for x in input().split())
    consumed = 1
    ava_bales = 0

    for i in range(iterations):
        curr_day, new_bales = (int(x) for x in input().split())
        ava_bales += new_bales

        for i in range(ava_bales):
            if curr_day <= day_num:
                consumed += 1
                curr_day += 1
                ava_bales -= 1
            else:
                continue

    print(consumed)

calculate()