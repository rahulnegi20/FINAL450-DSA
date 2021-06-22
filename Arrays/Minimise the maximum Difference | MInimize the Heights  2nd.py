# execution time : 1.26 s
def getMinDiff(self, arr, n, k):
    arr.sort()
    big, small = 0, 0
  #Tf  small = 0 
    best = arr[n-1] - arr[0]
    for i in range( n-1):
        small = min(arr[0] +k, arr[i+1] - k)
        big = max(arr[-1]-k, arr[i]+ k)
        if small <0 : continue
        best = min(best, big-small)

    return best
    
    
    #link = https://practice.geeksforgeeks.org/problems/minimize-the-heights3351/1#
