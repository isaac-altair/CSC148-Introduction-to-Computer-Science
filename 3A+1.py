def reduce(n):
    val = []
    if n == 1:
        return [n]
    else:
        val.append(n)
        if n % 2 == 0:
            return val + (reduce(n/2))
        else:
            return val + (reduce(n * 3 + 1))
