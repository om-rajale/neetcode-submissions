class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash_map = {}
        for i in range(len(nums)):
            if nums[i] not in hash_map:
                hash_map[nums[i]] = 1
            hash_map[nums[i]] += 1
        sorted_map = dict(sorted(hash_map.items(), key=lambda item: item[1],reverse=True))
        
        res = []
        for key ,value in sorted_map.items():
            res.append(key)
        
        return res[:k]

        
        
