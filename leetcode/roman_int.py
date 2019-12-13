def romanToInt(s: str) -> int:
    syntax = {'I' : 1, 'V' : 5, 'X' : 10, 'L' : 50, 'C' : 100, 'D' : 500, 'M' : 1000}
    i = 0
    result = 0
    while i < len(s):
        if i < len(s) - 1:
            key1 = syntax[s[i]]
            key2 = syntax[s[i+1]]

            if key2 > key1:
                result += key2 - key1
                i += 2
            else:
                result += key1
                i += 1
        else:
            key1 = syntax[s[i]]
            result += key1
            i += 1
    return result

print(romanToInt("IXVII"))