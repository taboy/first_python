#Сформировать список из  N членов последовательности.Для N = 5: 1, -3, 9, -27, 81 и т.д.
n= int(input("please write number"))
sum=1
for y in range(n):
    print(sum)
    sum=sum*-3
    