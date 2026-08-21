def aritmatika(a: int, n: int):
    to_list = []
    n += 1
    for i in range(a, n):    
        to_list.append(i)
    result = sum(to_list)
    return result
