# exe time : 0.43s 
def minJumps(self, arr, n):

    step, maxReach = arr[0], arr[0]
    jump = 1


    if n <= 1 : return 0 

    if arr[0] == 0 : return -1 

    for i in range(1, n):
        #checking if we reached last element
        if i == n-1 : return jump

        maxReach = max(maxReach, i + arr[i])

        step -= 1 
        #updaing jump
        if step == 0:
            jump += 1
            #IF the maxReach is 0/ -ve or smaller than i 
            if i >= maxReach: return -1 
            #updating step
            step = maxReach-i
            #returning answer
            if step >= len(arr) - i : return jump

      return 
      
#link  = https://practice.geeksforgeeks.org/problems/minimum-number-of-jumps-1587115620/1#
