def isPrime(n):
    if n<=1:
        return False
    elif n ==2 :
        return True
    else:
        for i in range(2,int(n**.5)+2):
            if(n%i==0):
                return False
        return True
# print(isPrime(4))
for i in range(100):
    print(i,isPrime(i))