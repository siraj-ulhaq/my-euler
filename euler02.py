def fib(n):
    if n == 1:
        return 1 
    elif n == 2:
        return 2
    elif n > 2:
        return fib(n-2) + fib(n-1)

def num():
    n = 1
    while fib(n) <= 4000000:
        n+=1
    return n

sum = 0
for i in range(1,num()):
    if fib(i) % 2 == 0:
        sum += fib(i)
    else:
        continue

print(sum)









