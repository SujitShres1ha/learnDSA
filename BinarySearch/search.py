import random

def search_list(list1,x):
    start = 0
    end = len(list1)-1
    
    asc = list1[start]<list1[end]
    while (start<=end):
        mid = (start+end)//2
        if (list1[mid] == x):
            return mid
        if (asc):
            if (x < list1[mid]):#[1,3,5,6,7,9]
                end = mid - 1
            else:
                start = mid + 1
        else:
            if (x < list1[mid]):
                start = mid + 1
            else:
                end = mid - 1
    return -1

def create_list(min,max,size):
    lst = [random.randint(min,max) for _ in range(size)]
    lst.sort()
    return lst

lst = create_list(0,5,5)
print(lst)
print(search_list(lst,3))