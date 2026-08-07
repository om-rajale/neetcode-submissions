from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # 1. Count frequencies using a hash map
        hash_map = {}
        for n in nums:
            hash_map[n] = hash_map.get(n, 0) + 1
            
        # 2. Sort the dictionary items by value (frequency) in descending order
        # We sort the items (key-value pairs) based on the frequency (x[1])
        sorted_items = sorted(hash_map.items(), key=lambda x: x[1], reverse=True)
        
        # 3. Extract the first k keys from the sorted list
        res = []
        for i in range(k):
            res.append(sorted_items[i][0])
            
        return res