#Подсчитать сумму цифр в вещественном числе.
n=int(input("write a number"))
b=0
while n>0:
    c=n%10
    n=n//10
    b=b+c
print(b)