y1=int(input("enter the future year : "))
y2=int(input("enter the current year : "))
print("leap year till now are :  ")
for i in range(y2,y1+1):
    if i%400==0:
        print(i)
    elif i%100==0:
        print("not a leap year ")
    elif i%4==0:
        print(i)

