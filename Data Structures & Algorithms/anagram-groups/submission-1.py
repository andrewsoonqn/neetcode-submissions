class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # keep a map of one anagram sorted : list of anagrams 
        hm = defaultdict(list)

        for s in strs:
            key = "".join(sorted(s))

            hm[key].append(s)

        ANS = [ss for ss in hm.values()]


        return ANS

