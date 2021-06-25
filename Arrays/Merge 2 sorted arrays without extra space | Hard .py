# execution time : 2.12s 
def merge(self, arr1, arr2, n, m):

    gap = n + m
    if gap <=1 :
        gap = 0
    gap = (gap//2) + (gap % 2 )

    while gap > 0:
        i = 0
        #traversing through arr1 
        while i + gap < n :
            if arr1[i] > arr1[i+gap]:
                arr1[i], arr1[i+gap] = arr1[i+gap], arr1[i]
            i += 1

        #traversing in both arr1 and arr2 
        j = gap - n if gap > n else 0
        while i < n and j < m:
            if arr1[i] > arr2[j]:
                arr1[i], arr2[j] = arr2[j], arr1[i]
            i += 1
            j += 1

        #traversing through arr2 in case m is bigger than n
        if j < m :
            j = 0
            while j + gap < m:
                if arr2[j] > arr2[j +gap]:
                    arr2[j], arr2[j+gap] = arr2[j+gap], arr2[j]
                j += 1

        if gap <=1 :
            gap = 0
        gap = (gap//2) + (gap % 2)
       
# Problem link : https://practice.geeksforgeeks.org/problems/merge-two-sorted-arrays5135/1#
