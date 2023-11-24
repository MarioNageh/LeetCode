class Solution(object):
    def licenseKeyFormatting(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        t = s.replace('-', '')
        ist_group_len = len(t) % k or k
        # 25g3j
        res = t[:ist_group_len].upper()
        for i in range(ist_group_len, len(t), k):
            res += '-' + t[i: i + k].upper()

        return res

#"5F3Z-2e-9-w"

print(Solution().licenseKeyFormatting("5F3Z-2e-9-w", 4))
