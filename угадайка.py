import random
a = 1
b = 1
print('сыграем с тобой в игру, я загадал число от 1 до 10, угадай его')
a = random.randint(1,10)
print('введи число')
b = int(input())
if a==b:
    print('правильно я загадал число ', a)
    
else:
        print('неправильно я загадал число ', a)
