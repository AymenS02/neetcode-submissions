class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = {}

        for word in strs:
            if "".join(sorted(word)) not in dic:
                dic["".join(sorted(word))] = [word]
            else:
                ke  = "".join(sorted(word))
                dic["".join(sorted(word))].append(word)
        
        return list(dic.values())