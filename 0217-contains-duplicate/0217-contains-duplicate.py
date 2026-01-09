"""class Solution(object):
    def containsDuplicate(self, nums:List[int])->bool:
        return len(set(nums)) < len(nums)
        """
"""
        :type nums: List[int]
        :rtype: bool
        """
    

class Solution(object):
   def containsDuplicate(self, nums):
      """
      :type nums: List[int]
      :rtype: bool
      """
      return not len(nums) == len(set(nums))
