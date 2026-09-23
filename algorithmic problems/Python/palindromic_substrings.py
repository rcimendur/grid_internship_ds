class Solution(object):
    def countSubstrings(self, s):
        total_pals = 0

        for i in range(len(s)):
            left = right = i

            while left >= 0 and right < len(s) and s[left] == s[right]:
                total_pals += 1
                left -= 1
                right += 1

            left = i
            right = i + 1

            while left >= 0 and right < len(s) and s[left] == s[right]:
                total_pals += 1
                left -= 1
                right += 1

            

