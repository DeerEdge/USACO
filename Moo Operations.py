num_cases = int(input())
for i in range(num_cases):
    test_case = input()
    bool_flag = True
    count = 0

    if test_case[0] == 'O':
        test_case[0] = 'M'
        count = count + 1

    if test_case[1] == 'M':
        bool_flag = False

    if test_case[len(test_case)-1] == 'M':
        test_case[len(test_case)-1] = '0'
        count = count + 1

