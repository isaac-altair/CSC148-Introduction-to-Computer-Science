def fibonacci(n: 'int') -> int:
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


def purdyprint(in_list, indentation=0) -> str:
    output = ""
    for item in in_list:
        if isinstance(item, list):
            output += purdyprint(item, indentation + 1)
        else:
            for i in range(0, indentation):
                output += "  "
            output += item + "\n"  
    return output
