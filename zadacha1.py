#Сдвинуть список на 1 элемент влево (последний становится первым).
a = (list(map(int, input().split())))
def zamena_elementa(a): 
    if a:
        last = a.pop() 
        a.insert(0, last) 
    return a
zamena_elementa(a)
print(a)