#Вывести на экран числа от -N до N
num=abs(int(input("please write first number")))
num2= int(input("please write second number"))
for y in range(-num,num2+1):
    print(y,end=" ")