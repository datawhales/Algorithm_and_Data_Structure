lst = [7,5,9,0,3,1,6,2,4,8]

def selection_sort(lst):
    for i in range(len(lst)):
        min_index = i
        for j in range(i+1, len(lst)):
            if lst[min_index] > lst[j]:
                min_index = j
        tmp = lst[min_index]
        lst[min_index] = lst[i]
        lst[i] = tmp
        # lst[i], lst[min_index] = lst[min_index], lst[i]
        # print(lst)
    return lst
print('sorting 결과는..')
print(lst)
import time
start = time.time()
print(selection_sort(lst))
print(f'실행 시간은 {time.time() - start}입니다.')