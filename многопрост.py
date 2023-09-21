a = 1
b = 1
c = 0
d = 0
count = 2
print('введите чиcла,а я проверю промежуток между ними на наличие простых чисел')
a = int(input())
d = int(input())
for i in range(a,d):
    if i ==1:
      print()  
    else:
        count = 2
        c = 0
        while count < i:
            b = i % count
            count = count + 1
            if b == 0:
                c = 1
        if c == 0:
            print(i)

i = i + 1
while count < i:
    b = i % count
    count = count + 1
    if b == 0:
        c = 1
if c == 0:
    print(i)

print('простые числа на промежутке от',a,'до',d)
