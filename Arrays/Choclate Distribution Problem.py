# exe time : 1.1s 
    def findMinDiff(self, A,N,M):

        A.sort() #sorting 
        best = float('inf') #a very large number
        
        if N == M : #corner case
            return A[N-1] - A[0]
        
        for i in range(N-M+1):
            best = min(A[M+i-1]- A[i], best) #slidig window 

        return best
      
      
 #problem link : https://practice.geeksforgeeks.org/problems/chocolate-distribution-problem3825/1#
