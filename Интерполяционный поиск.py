import random

n=40
arr=[]
for i in range(n):
    number=random.randint(0,100)
    arr.append(number)

to_search=random.randint(1,100)
answer=-1

arr.sort()
left=0
right=len(arr)-1
print(arr)
print(to_search)

while left<=right and to_search>=left and to_search<=right:
    part1=float(right-left)/(arr[right]-arr[left])
    part2=to_search-arr[left]
    index=left+int(part1*part2)
    
    if arr[index]==to_search:
        answer=index
        break
    else:
        if arr[index]>to_search:
            last=index-1
        else:
            first=index+1

if answer!=-1:
   print(f'Элемент в списке найден. Его индекс {answer}')
else:
   print(f'Элемент в списке отсутствует')