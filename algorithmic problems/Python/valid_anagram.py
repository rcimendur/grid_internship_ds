class Solution(object):
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False

        char_count = {}

        for i in range(len(s)):
            char_count[s[i]] = char_count.get(s[i], 0) + 1
            char_count[t[i]] = char_count.get(t[i], 0) - 1

        for val in char_count.values():
            if val != 0:
                return False

        return True