
def quicksort(alist):
    if len(alist) == 1 or len(alist) == 0:
        return alist
    else:
        pivot = alist[0]
        i = 0
        for j in range(len(alist)-1):
            if alist[j+1] < pivot:
                alist[j+1],alist[i+1] = alist[i+1], alist[j+1]
                i += 1
        alist[0],alist[i] = alist[i],alist[0]
        first_part = quicksort(alist[:i])
        second_part = quicksort(alist[i+1:])
        first_part.append(alist[i])
        return first_part + second_part
        
alist = [54,26,93,17,77,31,44,55,20]
print(quicksort(alist))
print(alist)