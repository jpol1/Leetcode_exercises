def left(idx): #Theta(1)
    return 2*idx + 1

def right(idx): # Theta(1)
    return 2*idx + 2
    
def parent(idx): # Theta(1)
    if idx % 2 == 1 :
        return idx // 2 
    return idx // 2 - 1
 
def max_heapify(arr, idx): # O(logn)
    l = left(idx)
    r = right(idx)
    
    n = len(arr)
    
    if l >= n:
        largest = idx
        
    elif r >= n:

        if arr[idx] > arr[l]:
            largest = idx
        else:
            largest = l
            
    else:
        
        if (arr[l] < arr[r]):
            suspect = r
        else:
            suspect = l
        
        if arr[idx] > arr[suspect]:
            largest = idx
        else:
            largest = suspect

    if largest != idx:
        arr[idx], arr[largest] = arr[largest], arr[idx]
        max_heapify(arr, largest)

def get_max(arr): #O(logn)
    elem = arr[0]
    arr[0] = arr[-1]
    arr.pop()
    max_heapify(arr, 0)
    return elem

def build_max_heap(arr): #O(n)
    for i in range(len(arr)//2 - 1, -1, -1):
        max_heapify(arr, i)
        

def max_heap_insert(arr, elem): # O(logn)
    arr.append(elem)
    i = len(arr) - 1
    while i > 0 and arr[parent(i)] < arr[i]:
        arr[i], arr[parent(i)] = arr[parent(i)], arr[i]
        i = parent(i)


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        build_max_heap(stones) 
        while len(stones) > 1: 
            max_elem = get_max(stones)
            second_max = get_max(stones)
            
            if max_elem != second_max:
                max_heap_insert(stones, max_elem-second_max)
                
        
        return 0 if len(stones) == 0 else stones[0]
            