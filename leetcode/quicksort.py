def quicksort(l, start=0, end=None):
    if end is None:
        end = len(l) - 1

    if start < end:
        pivot = partition(l, start, end)
        quicksort(l, start, pivot - 1)
        quicksort(l, pivot + 1, end)

def partition(l, start, end):
    pivot = l[end]
    lt_iter = start
    
    for i in range(start, end):
        if l[i] <= pivot:
            l[i], l[lt_iter] = l[lt_iter], l[i]
            lt_iter += 1
        
    l[end], l[lt_iter] = l[lt_iter], l[end]
    return lt_iter
    
l = [1, 5, 2, 453, 2, 5, 7]
quicksort(l)
print(l)