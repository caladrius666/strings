def z_function(s):
    res = []
    i = 1
    l = len(s)
    res.append(0)
    while i < l:
        left, right = 0, i
        while right < l and s[left] == s[right]:
            left += 1
            right += 1
        res.append(left)
        i += 1
    return res

string = input()
print(" ".join(map(str, z_function(string))))
