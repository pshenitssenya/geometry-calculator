s = input("Введите строку: ")
def compress_with_methods(s):
    if not s:
        return s
    result = ""
    i = 0
    while i < len(s):
        ch = s[i]
        j = i
        while j < len(s) and s[j] == ch:
            j += 1
        count = j - i
        result += ch + str(count)
        i = j
    return result if len(result) < len(s) else s
print("Результат:", compress_with_methods(s))