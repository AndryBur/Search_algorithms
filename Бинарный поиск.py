import random

n=40
arr=[]
for i in range(n):
    number=random.randint(0,100)
    arr.append(number)

to_search=random.randint(1,100)
answer=-1

arr.sort()
first=0
last=n-1
print(arr)
print(to_search)

while first<=last and answer==-1:
    mid_index=(first+last)//2
    if arr[mid_index]==to_search:
        answer=mid_index
    else:
        if arr[mid_index]>to_search:
            last=mid_index-1
        else:
            first=mid_index+1

if answer!=-1:
   print(f'Элемент в списке найден. Его индекс {answer}')
else:
   print(f'Элемент в списке отсутствует')



