'''class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        '''
class Solution (object):
    def isAnagram(self,s,t):
        to=sorted(t)
        so=sorted(s)
        if to==so:
            return True
        else:
            return False