
def Fizzbuzz(n:int):
    for i in range(1, n + 1):
        if i % 3 == 0 or i % 5 == 0:
            print('Fizzbuzz')

        elif i % 3 == 0:
            print('Fizz')

        elif i % 5 == 0:
            print('Buzz')

        else:
            print(i)


Fizzbuzz(50)