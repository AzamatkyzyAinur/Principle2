def squares_up_to_N(N):

    for i in range(N + 1):

        yield i * i

N = int(input())

for square in squares_up_to_N(N):

    print(square)
 
