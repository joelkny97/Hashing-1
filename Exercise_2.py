# Time Complexity: O(n)
# Space Complexity: O(1)
# Were you able to run the code on Leetcode: Yes
# Any problem you faced while coding this: No

from collections import defaultdict

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        
        if len(s)!=len(t):
            return False

        # create two hashmaps to store bidirectional mappins
        smap = defaultdict(lambda: None)
        tmap = defaultdict(lambda: None)

        for i in range(len(s)):
            sChar = s[i]
            tChar = t[i]

            # if current S char does not exist then store the mapping along with char from T
            if not smap[sChar]:
                smap[sChar] = tChar
            else:
                # if char exists but is not the same as current T char then return False
                if smap[sChar] != tChar:
                    return False
            
            # if current T char does not exist then store the mapping along with char from S
            if not tmap[tChar]:
                tmap[tChar] = sChar
            else:
                # if char exists but is not the same as current S char then return False
                if tmap[tChar] != sChar:
                    return False 
            

        return True

