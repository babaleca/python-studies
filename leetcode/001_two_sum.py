class Solution(object):
    def twoSum(self, nums, target):
        for i in range(0, len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i]+nums[j]==target:
                    return [i,j]

   #meu primeiro submit no LeetCode O(n^2), resolvi mas descobri que há um jeito mais otimizado.              

        
        