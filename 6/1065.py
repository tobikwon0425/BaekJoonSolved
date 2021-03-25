def distic_module(compare: int) -> bool:
    compare_str = str(compare)
    TnF = False
    pre_num = None
    diff = None

    for i in range(len(compare_str)):
            if pre_num is None:
                pre_num = int(compare_str[i])
            elif diff is None:
                diff = pre_num - int(compare_str[i])
                pre_num = int(compare_str[i])
            else:
                if diff == pre_num - int(compare_str[i]):
                    TnF = True

                pre_num = int(compare_str[i])
    
    if TnF is True:
        return True
    return False


def function() :
    n = int(input())

    count = 0

    if n < 100:
        count = n
    else:
        count = 99

        for i in range(100, n+1):
            if distic_module(i) is True:
                count += 1

    print(count)

function()
