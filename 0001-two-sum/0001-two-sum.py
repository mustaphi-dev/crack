class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        N = len(nums)

        hmap = {}

        for i in range(N):
            diff = target - nums[i] 
            if diff in hmap:
                return [i, hmap[diff]]

            else:
                hmap[nums[i]] = i
                
        