lst = [5,7,9,0,3,1,6,2,4,8]

def quick_sort(lst, start, end):
    if start >= end:
        return
    pivot = start
    left = start + 1
    right = end
    while left <= right:
        while left <= end and lst[left] <= lst[pivot]:
            left += 1
        while right > start and lst[right] >= lst[pivot]:
            right -= 1
        if left > right:
            lst[pivot], lst[right] = lst[right], lst[pivot]
        else:
            lst[left], lst[right] = lst[right], lst[left]
    quick_sort(lst, start, right-1)
    quick_sort(lst, right+1, end)
    return lst

def quick_sort2(lst):
    if len(lst) <= 1:
        return lst
    pivot = lst[0]
    tail = lst[1:]

    left_part = [x for x in tail if x <= pivot]
    right_part = [x for x in tail if x > pivot]
    return quick_sort2(left_part) + [pivot] + quick_sort2(right_part)

print('sorting 결과는..')
print(lst)
import time
start = time.time()
print(quick_sort(lst, 0, len(lst)-1))
print(f'실행 시간은 {time.time() - start}입니다.')
start = time.time()
print(quick_sort2(lst))
print(f'실행 시간은 {time.time() - start}입니다.')