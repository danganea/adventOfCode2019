from collections import Counter
def good(nr):
    return bool(set(Counter(str(nr)).values()) & {2})
    # Or do this, which is less convoluted :)
    # return any(list(str(nr)).count(str(i)) == 2 for i in range(10))

def solution(left,right):
    return sum(1 for x in range(left,right) if list(str(x)) == sorted(str(x))
    and any(a == b for (a,b) in zip(str(x),str(x)[1:])))

def solution2(left,right):
    return sum(1 for x in range(left,right) if list(str(x)) == sorted(str(x))
    and good(x))

print(solution2(146810,612564 + 1))