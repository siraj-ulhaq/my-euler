
def multiples(n):
    """ Finds the sum of multiples of 3 and 5 below n"""
    list = []
    for i in range(1, n):
        if (i % 3 == 0) or (i % 5 == 0):
            list.append(i)
    sum = 0
    for num in list:
        sum += num
    print(sum)

multiples(1000)
    