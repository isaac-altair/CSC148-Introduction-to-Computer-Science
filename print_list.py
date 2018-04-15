def print_list(lst: 'list') -> None:
    print(lst.pop())
    if len(lst) != 0:
        return print_list(lst)
