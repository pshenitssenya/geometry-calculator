# перестановки списка (без itertools)
def permutations(nums):
    result = []
    n = len(nums)
    used = [False] * n # какие индексы уже взяты
    path = [] # текущая строящаяся перестановка
    def backtrack():
        if len(path) == n:
            result.append(path[:])   # копия, иначе все ссылки на один список
            return
        for i in range(n): # Перебор вариантов
            if used[i]:
                continue
            # выбрать
            used[i] = True
            path.append(nums[i])
            backtrack()
            # отменить выбор (backtrack)
            path.pop()
            used[i] = False
    backtrack()
    return result
# проверка
print(permutations([1, 2, 3]))
