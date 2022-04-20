#Сообщить в какой четверти координатной плоскости или на какой оси находится точка с координатами Х и У 
x = int(input("print x "))
y = int(input("print y "))
if x<0 and y<0:
    print("3")
elif x<0 and y>0:
    print("2")
elif x>0 and y>0:
    print("1")
elif x>0 and y<0:
    print("4")
