def countdown_n(n):

    for i in range(n, -1, -1):

        yield i

n = int(input())

for num in countdown_n(n):

    print(num)
 