


from re import X


def prime_numbr(x,y):
    prime_list =[]
    for i in range(x,y):
        if i == 0 | i == 1:
            continue
        elif i == 2:
            prime_list.append(i)
            continue
        else:
            for j in range(2,int((i/2)+1)):
                if i % j == 0:
                    break
            else:
                prime_list.append(i)

    return prime_list

def isPrime(x):
    if x <2:
        return 0
    else:
        for i in range(2, int((x/2)+1)):
            if x%i == 0:
                return 0
                break
        else:
            return 1

'''    
x = int(input("enter starting numbr : " ))
y = int(input("enter finishing numbr : " ))
n = prime_numbr(x,y)
print(n) if len(n) != 0 else print('no primes')
'''
x = int(input("enter the numbr : " ))

print("Is prime ") if isPrime(x) == 1 else print('Not prime')