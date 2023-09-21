a = 1
b = 1
c = 0
count = 2
print('введите число, а я проверю простое ли оно')
a = int(input())
if a ==1:
    print('это число не простое')
else:
    while count < a:
        b = a % count
        count = count + 1
        if b == 0:
            c = 1
    if c == 0:
        print('это число простое')
    else:
        print('это число не простое')
