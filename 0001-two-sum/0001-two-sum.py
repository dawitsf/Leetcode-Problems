class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """ 
        seen=set()
        idx=[]
        for k in range(len(nums)):
            if target-nums[k] in seen:
                idx.append(k)
                idx.append(nums.index(target-nums[k]))
            else:
                seen.add(nums[k])
        return idx
                
                



        