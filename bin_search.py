##def bin_search(L,x):
##    while len(L) > 1:
##        mid = len(L) // 2
##        if x <= L[mid]:
##            L = L[mid:]
##        else:
##            if x >= L[mid]:
##                L = L[:mid]
##            
##    return len(L) > 0 and L[0] == x

def binary_search(l, value):
    low = 0
    high = len(l)-1
    while low <= high: 
        mid = int(low+high)//2
        if l[mid] > value:
            high = mid-1
        elif l[mid] < value:
            low = mid+1
        else:
            return mid
    return -1
