class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        word=str(x)
        reverse=word[::-1]
        return word==reverse

