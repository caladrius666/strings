def prefix_function(string):
    L = len(string)
    res = [0]*L
    for i in range(1, L):
        k = res[i-1]
        while k > 0 and string[k] != string[i]:
            k = res[k-1]
        if string[k] == string[i]:
            k += 1
        res[i] = k
    return res

string = input()
print(" ".join(map(str, prefix_function(string))))
