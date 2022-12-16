num=int(input("Enter Number:"))

try:
    if(num >= 10 and num <=30):
        print("Num is between 10 and 30")
    else:
        raise Exception

except Exception:
    if (num<10):
        print("Range of number should not be smaller than 10")
    elif (num>30):
        print("Range of number should not be greater than 30")


