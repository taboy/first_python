#Для натурального n создать словарь индекс-значение, состоящий из элементов последовательности 3n + 1.
#Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}
n=int(input("write number n"))
for y in range(1,n+1):
    print(f"{y}:{3*y+1}")