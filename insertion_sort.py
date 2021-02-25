lst = [7,5,9,0,3,1,6,2,4,8]

def insertion_sort(lst):
    for i in range(1, len(lst)):
        for j in range(i, 0, -1):
            if lst[j] < lst[j-1]:
                lst[j], lst[j-1] = lst[j-1], lst[j]
            else:
                break
        # print(lst)
    return lst

print('sorting 결과는..')
print(lst)
import time
start = time.time()
print(insertion_sort(lst))
print(f'실행 시간은 {time.time() - start}입니다.')