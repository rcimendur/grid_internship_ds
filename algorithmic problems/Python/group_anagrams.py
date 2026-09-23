class Solution(object):
    def groupAnagrams(self, strs):
        angs = {}

        for word in strs:
            count = [0] * 26

            for char in word:
                count[ord(char) - ord('a')] += 1

            signature = tuple(count)

            if signature not in angs:
                angs[signature] = []

            angs[signature].append(word)

        return list(angs.values())