class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # keep a map of one anagram sorted : list of anagrams 
        hm = defaultdict(list)

        for s in strs: # n iterations
            key = "".join(sorted(s)) # Theta(1)

            hm[key].append(s) # O(1), O(1)

        return [ss for ss in hm.values()] # O(n)

# time complexity: O(n)