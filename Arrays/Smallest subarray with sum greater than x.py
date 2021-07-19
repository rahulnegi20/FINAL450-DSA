# exe time : 0.6s 
def sb(self, a, n, x):
    start = end = total = 0 
    best = float('inf')

    while end < n :
        if a[end] > x :
            return 1 
        total += a[end]

        while total > x :
            best = min(best, end - start)
            total -= a[start]
            start += 1 
        end += 1

    return best+1
  
  #problem link : https://practice.geeksforgeeks.org/problems/smallest-subarray-with-sum-greater-than-x5651/1#
