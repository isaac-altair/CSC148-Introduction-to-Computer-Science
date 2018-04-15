def heap_remove (heap:'list'):
    top = heap[0]
    heap[0] = heap[:-1]
    del heap[-1]
    if len(heap) == 1:
        heap_false = False
    else:
        heap_false = True
    index = 0
    while heap_false:
        if (2*index +1) <= len(heap)-1:
            if (2*index +2) <= len(heap)-1:
                if heap[2 * index + 1] < heap[2 * index +2]:
                    min_val = 2*index+ 1
                else:
                    min_val = 2*index +2
                if heap[index] > heap[min_val]: # the issue is that min_value is an int where as heap[index] is an index
                    heap[index], heap[min_val] = heap[min_val], heap[index]
                    index = min_val
                else:
                    heap_false = False
 
            else:
                if heap[index] > heap[2*index+ 1]:
                    heap[index], heap[2*index+ 1] = heap[2*index+ 1], heap[index]
                    index = min_value
                else:
                    heap_false = False
        else:
            heap_false = False
    return top
