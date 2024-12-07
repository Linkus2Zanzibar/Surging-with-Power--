def power2(number):
    if number <=0:
        return False
    return (number&(number-1))==0
n=int(input(" Enter a number "))
if(power2(n)):
    print("The number is power of 2")
else:
    print("The number is NOT a power of 2 ")

    