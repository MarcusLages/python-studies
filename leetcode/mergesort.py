def mergesort(l):
    if len(l) <= 1:
        return l

    half = len(l) // 2
    left = l[:half]
    right = l[half:]
    
    l_sorted = mergesort(left)
    r_sorted = mergesort(right)
    return merge(l_sorted, r_sorted)

def merge(left, right):
    res = []
    i = 0
    j = 0
    
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            res.append(left[i])
            i += 1
        else:
            res.append(right[j])
            j += 1
    
    res.extend(left[i:])
    res.extend(right[j:])

    return res
        

l = [1, 5, 2, 453, 2, 5, 7]
print(mergesort(l))