a=int(input("Enter the number : "))
def prime(a):
    (result,i)=(True,2)
    while (result and (i<a)):
        if (a%i==0):
            result =False
        i+=1
    return result
print(prime(a))