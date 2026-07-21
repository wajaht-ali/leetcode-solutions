# ────────────────────────────────────────────────────────────
# Problem   : 0824. Goat Latin
# URL       : https://leetcode.com/problems/goat-latin/
# Difficulty: Easy
# Tags      : String
#
# Runtime   : 0 ms
# Memory    : 19.2 MB
# Language  : Python3
# Submitted : 2026-07-21T18:07:46.558Z
#
# Examples
# ────────
# Example 1:
#
# Input: sentence = "I speak Goat Latin"
# Output: "Imaa peaksmaaa oatGmaaaa atinLmaaaaa"
#
# Example 2:
#
# Input: sentence = "The quick brown fox jumped over the lazy dog"
# Output: "heTmaa uickqmaaa rownbmaaaa oxfmaaaaa umpedjmaaaaaa overmaaaaaaa hetmaaaaaaaa azylmaaaaaaaaa ogdmaaaaaaaaaa"
#
# Constraints
# ───────────
# Constraints:
#
# • 1 <= sentence.length <= 150
#
# • sentence consists of English letters and spaces.
#
# • sentence has no leading or trailing spaces.
#
# • All the words in sentence are separated by a single space.
#
# ────────────────────────────────────────────────────────────

class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        #rules
        # 1. Split the string
        # 2. check each word with what char it starts
        # 3. Apply conditions
        # 4. join it

        s = sentence.split()
        vowels = "aeiouAEIOU"
        cnt = 1
        ans = ""
        for ch in s:
            if ch[0] in vowels:
                ch = ch + 'ma'
                i = 0
                while i < cnt:
                    ch = ch + 'a'
                    i += 1
                cnt +=1
                ans = ans + ' ' + ch
            else:
                ch = ch[1:] + ch[0] + 'ma'
                i = 0
                while i < cnt:
                    ch = ch + 'a'
                    i += 1
                cnt +=1
                ans = ans + ' ' + ch

        return ans.strip()
            
