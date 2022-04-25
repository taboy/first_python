#Сформировать список из  N членов последовательности.Для N = 5: 1, -3, 9, -27, 81 и т.д.
n= int(input("please write number"))
sum=1
list=[]
for y in range(n):
    list.append(sum)
    sum=sum*-3
print(list)