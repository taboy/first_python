#Для натурального n создать словарь индекс-значение, состоящий из элементов последовательности 3n + 1.
num=int(input("please write number"))
dict={}
for y in range(num):
    n=y+1
    dict.update({n:3*n+1})
print(dict)
