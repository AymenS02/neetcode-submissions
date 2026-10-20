class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dictor = {}
        for i in nums:
            if i not in dictor:
                dictor[i] = 1
            else:
                dictor[i] += 1

        check = sorted(dictor, key=lambda num: dictor[num], reverse=True)

        return check[:k]
