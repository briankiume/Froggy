def soln(x, y, d):
    jumps = list(range(x, y, d))
    if jumps[-1] < y:
        jumps.append(d + jumps[-1])
    jumps.remove(x)
    num_jumps = len(jumps)
    return num_jumps


print(soln(10, 85, 30))
