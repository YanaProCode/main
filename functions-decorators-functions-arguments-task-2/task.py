def union(*args) -> set:
    a = set(args[0])
    b = set(args[1])
    union_func = a.union(b)
    return union_func
    raise NotImplementedError("Implement me!")


def intersect(*args) -> set:
    a = set(args[0])
    b = set(args[1])
    c = set(args[2])
    intersect_func = a.intersection(b,c)
    return intersect_func
    raise NotImplementedError("Implement me!")

print(union(('S', 'A', 'M'), ['S', 'P', 'A', 'C']))
print(intersect(('S', 'A', 'C'), ('P', 'C', 'S'), ('G', 'H', 'S', 'C')))