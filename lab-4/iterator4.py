def squares_ab(a, b):

    for i in range(a, b + 1):

        yield i * i

a = int(input())

b = int(input())

for sq in squares_ab(a, b):

    print(sq)
 
