n=int(input("Enter the number : "))
def prime(n):
    result=True
    for i in range(2,n):
        if n%i==0:
            result = False
            break
    return result
print(prime(n))
