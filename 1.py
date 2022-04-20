#По двум заданным числам проверить является ли одно квадратом второго 
a= int(input("write first number"))
b= int(input("write second number"))
if a==b**2 or b==a**2:
    print(f' yes {b} is {a}  square')
else:
    print("no")
