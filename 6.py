#Дано число обозначающее день недели. Вывести его название и указать является ли он выходным.
week=["weeked","monday","thuesday","wednesday","thursday","friday","saturday","sunday"]
num=abs(int(input("please write number of day")))
if num>7 or num<0:
    print("please write a number of day from 1 to 7")
elif num>0 or num<7:
    if num<6:        
        print(f"{week[num]} its not {week[0]}")
    else:
        print(f"{week[num]} its  {week[0]}")
