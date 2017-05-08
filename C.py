def find(sub, main):
    l = len(sub)
    result = []
    for i in range(len(main)-len(sub)+1):
        if main[i:i+l] == sub:
            result.append(i)
    if len(result) == 0:
        return [-1]
    else:
        return result


print(*find(input(), input()))
