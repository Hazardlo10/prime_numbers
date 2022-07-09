y = int(input('Введите начало интервала: '))
x = int(input('Введите число для проверки: '))

def is_prime_old(x):
    d = False
    for i in range(2, x):  # проверка на простое
        if i * i > x and not d:
            break
        if x % i == 0:
            print("Составное", i)
            d = True
    if not d:  # d==False
        print("Простое")
    return


def is_prime(x):
    for i in range(2, x):  # проверка на простое
        if i * i > x:
            break
        if x % i == 0:
            return False
    return True


for i in range(y, x+1):
    if is_prime(i):
        print(i)

#is_prime(x)
