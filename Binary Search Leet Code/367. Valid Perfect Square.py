class Solution:
    def isPerfectSquare(self, num):

        root = num**(0.5)

        if root//1 == root:
            return True
        return False

ans = Solution()
n = 16
print(ans.isPerfectSquare(n))
