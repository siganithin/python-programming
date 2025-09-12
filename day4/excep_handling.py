try:
    x=int(input("Enter the value of x:"))
    y=int(input("Enter the value of y:"))
    res=x/y
    print(res)
except ZeroDivisionError:
    print("Error occured...!")
else:
    print("Program excecuted successfully..")
finally:
    print("Thank u..")