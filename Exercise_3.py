# Time Complexity: O(n)
# Space Complexity: O(n)
# Were you able to run the code on Leetcode: Yes
# Any problem you faced while coding this: No

from itertools import zip_longest
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s = s.split()


        # create all possible pairs of pattern and s
        # and check if the number of unique elements in pattern, s and pairs are equal
        # if they are equal then it is a valid mapping
        # if not then it is not a valid mapping
        return (len(set(pattern)) ==
                len(set(s)) ==
                len(set(zip_longest(pattern,s))))
        
        # zip_longest - zips based on the larger of the two iterators
        
