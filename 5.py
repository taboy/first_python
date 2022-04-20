#Дано число. Проверить кратно ли оно 5 и 10 или 15 но не 30
num = int(input("please write number"))
if (num%5==0 and num%10==0 or num%15==0) and num%30!=0:
    print ("yes everything is fine ")
else:
    print("we have problem")
    