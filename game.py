import random
def is_valid(n):
    if n<1 or n>100:
        return False
    else:
        return True



d = True
cnt = 0

while d:
    n = int(input())
    a = random.randint(1,100)
    while is_valid(n) == False:
        print('Введите еще раз')
        n = int(input())
    while a != n:
    
        if n >a:
            print('Слишком много, попробуйте еще раз')
            n = int(input())
            cnt+=1
        elif n<a:
            print('Слишком мало, попробуйте еще раз')
            n = int(input())
            cnt += 1

    if a ==n:
        print('Вы угадали, поздравляем!')
        print('Kоличество попыток',cnt)
        print('Спасибо, что играли в числовую угадайку. Еще увидимся...')
        s = int(input('Повторить? \nДа = 1 \nНет = 2 \n'))
        if s == 1:
            d = True
            cnt = 0
        elif s == 2:
            d = False
'''
import random
n = int(input())
a = random.randint(1,100)
cnt = 0
l = 1
r = n
m = 50
while n!= m:
    m = (l + r)//2
    if m >n:
        print('Слишком много, попробуйте еще раз')
        r= m -1
        cnt+=1
    elif m<n:
        print('Слишком мало, попробуйте еще раз')
        l = m+1
        cnt += 1

if n ==m:
    print('Вы угадали, поздравляем!')
    print(cnt)
'''
