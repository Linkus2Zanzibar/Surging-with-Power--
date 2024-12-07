def power4(number):
    count=0
    if(number&(~(number&(number-1)))):
        while(number>1):
            number>>=1
            count=count+1
        if(count%2==0):
            return True
        else:
            return False
n=int(input(" Enter a number "))
if(power4(n)):
    print("The number IS a power of 4")
else:
    print("The number IS NOT a power of 4")