#Указав номер четверти прямоугольной системы координат, показать допустимые значения координат для точек этой четверти
coor= int(input("please write coor"))
if coor >4 and coor<1:
    print("please write number from 1 to 4")
elif coor ==1:
    print("x>0,y>0")
elif coor ==2:
    print("x>0,y<0")    
elif coor ==3:
    print("x<0,y<0")
elif coor ==4:
    print("x>0,y<0")