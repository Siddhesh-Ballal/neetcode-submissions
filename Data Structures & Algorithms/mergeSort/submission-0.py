# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:
        
        
        def mergesort(arr, s, e):
            if e - s + 1 <= 1:
                return arr 
            m = (s + e) // 2
            mergesort(arr, s, m)
            mergesort(arr, m + 1, e)
            merge(arr, s, m, e)
            return arr
        
        def merge(arr, s, m, e):
            l = arr[s : m + 1]    # left subarray
            r = arr[m + 1 : e + 1]    # right subarray

            i = 0   # for left subarray
            j = 0   # for right subarray
            k = s   # for merged array
            while i < len(l) and j < len(r):
                if l[i].key <= r[j].key:
                    arr[k] = l[i]
                    i += 1
                    k += 1
                else:
                    arr[k] = r[j]
                    j += 1
                    k += 1

            while i < len(l):
                arr[k] = l[i]
                i += 1
                k += 1
            while j < len(r):
                arr[k] = r[j]
                j += 1
                k += 1
        
        mergesort(pairs, 0, len(pairs))
        return pairs