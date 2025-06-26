from collections import Counter, defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        if len(strs)==0:
            return [[""]]
        # 1st method: using Counter to form anagram key
        # Time Complexity: O(n * k) where n is the number of strings and k is the maximum length of a string
        # Space Complexity: O(n * k) for storing
        # mapped = [Counter(i) for i in strs]
        # res = []
        
        # for i in range(len(mapped)):
            
        #     if strs[i]==0:
        #         continue
        #     key = [strs[i]]
            
        #     for j in range(i+1, len(mapped)):
                
        #         if mapped[j] == mapped[i]:
        #             key.append(strs[j])
        #             strs[j]=0
                
        #     res.append(key) 

        # return res if len(res)>0 else [[""]]

        # 2nd method : using sorted string to form anagram key 
        # Time Complexity: O(n * k log k) where n is the number of strings and k is the maximum length of a string
        # Space Complexity: O(n * k) for storing the result
        # res = defaultdict(list)

        # for i in strs:
        #     key = "".join(sorted(i))
        #     res[key].append(i)

        # return [i for i in res.values() ]

        # 3rd method: using hashed primed product for anagram key
        # Time Complexity: O(n * k) where n is the number of strings and k is the maximum length of a string
        # Space Complexity: O(n) for storing the result

        prime_map = defaultdict(list)
        
        def prime_product(s: str):
            primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101]
            res = 1
            for i in s:
                res*=(primes[ord(i)-97])

            return res

        for word in strs:
            key = prime_product(word)
            prime_map[key].append(word)

        return list(prime_map.values())



    






