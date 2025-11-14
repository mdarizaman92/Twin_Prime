def co_factor(n):
    co_factor_list=[]
    for i in range(1,n+1):
        if n%i==0:
            co_factor_list.append(i)
    return co_factor_list
def prime(n):
    return len(co_factor(n))==2
def first_prime(m):
    (count,i,prime_list)=(0,1,[])
    while (count<m):
        if prime(i):
            (count,prime_list)=(count+1,prime_list+[i])
        i+=1
    return prime_list
a=int(input("Enter the number : "))
print(first_prime(a))