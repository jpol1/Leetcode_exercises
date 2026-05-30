def left_f(idx): #Theta(1)
    return 2*idx + 1

def right_f(idx): # Theta(1)
    return 2*idx + 2
    
def parent(idx): # Theta(1)
    if idx % 2 == 1 :
        return idx // 2 
    return idx // 2 - 1
    
def max_heapify(arr, i): # O(log(n))
    left = left_f(i)
    right = right_f(i)
    n = len(arr)
    
    if left >= n:
        greatest = i
    elif right >= n:
        greatest = left if arr[left][1] > arr[i][1] else i
    else:
        suspect = left if arr[left][1] > arr[right][1] else right
        greatest = suspect if arr[suspect][1] > arr[i][1] else i
    
    if greatest != i:
        arr[greatest], arr[i] = arr[i], arr[greatest]
        max_heapify(arr, greatest)

def build_max_heap(arr): #O(n/2)
    for i in range(len(arr)//2 - 1, -1, -1):
        max_heapify(arr, i)
        
def get_max(arr): # O(logn) przez max_heapify
    elem = arr[0]
    arr[0] = arr[-1]
    arr.pop()
    if len(arr) > 0:
        max_heapify(arr, 0)
    return elem
    
def insert_elem(arr, elem): #O(logn)
    arr.append(elem)
    i = len(arr) - 1
    while i > 0 and arr[i][1] > arr[parent(i)][1]:
        arr[i], arr[parent(i)] = arr[parent(i)], arr[i]
        i = parent(i)
    

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        # u - liczba wszystkich zadań (maksymalnie jest 26 tyle co liter)
        # m - wszystkich elementów w liście
        # k - cooldown (w funkcji n) 
        
        # Czas wykonania funkcji T(u,k,m,C) = Theta(m) + Theta(u) + O(u) + O(m*k) * ( O(log u) + O(k) + O(log u) ) = O(m*k * (log u + k))

        heap = []
        time_queue = [None]*(n) #Miejsca alokujemy k 
        counter = {}
        res = 0
        
        for task in tasks: # Theta(m)
            if task in counter:
                counter[task] += 1
            else:
                counter[task] = 1
        
        for key, value in counter.items(): #Theta(u)
            heap.append([key, value])
            
        build_max_heap(heap) #O(u)
        
        while(heap or not all(elem is None for elem in time_queue)): #Pętla wykona się maksymalnie m*k razy jeśli u == 1 czyli O(m*k)
            tmp = None 
            if heap: 
                tmp = get_max(heap) # O(log u)
                tmp[1] -= 1 
                if tmp[1] == 0: 
                    tmp = None 
            
            time_queue.insert(0, tmp) #O(k)
            
            back_heap = time_queue.pop()
            
            if back_heap and back_heap[1] > 0:
                insert_elem(heap, back_heap) #O(log u)
                
            res += 1
        
        return res