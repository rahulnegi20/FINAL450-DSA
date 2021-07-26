#exe : 44ms 
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        first_index = -1
        second_index = -1
        
        # finding any ascending number(sequence)
        for i in range(len(nums)-1):
          if nums[i] < nums[i+1]:
            first_index = i
            
        # if not means its descending order need to reverse 
        if first_index == -1:
          nums.reverse()
          return
        
        # swaping first_index with greater number 
        for i in range(first_index+1, len(nums)):
          if nums[first_index] < nums[i]:
            second_index = i
        
        #swaping 
        nums[first_index], nums[second_index] = nums[second_index], nums[first_index]

       #sorting the rest of array because we need next permutation only!
        nums[first_index+1:] = sorted(nums[first_index+1:])

        
 # link : https://leetcode.com/problems/next-permutation/submissions/
                
