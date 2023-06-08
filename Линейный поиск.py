import random

n=40
arr=[]
for i in range(n):
    number=random.randint(0,100)
    arr.append(number)

to_search=random.randint(1,100)
answer=-1
print(arr)
print(to_search)
for i in range(n):
    if arr[i]==to_search:
        answer=i
        break

if answer!=-1:
   print(f'Элемент в списке найден. Его индекс {answer}')
else:
   print(f'Элемент в списке отсутствует')
