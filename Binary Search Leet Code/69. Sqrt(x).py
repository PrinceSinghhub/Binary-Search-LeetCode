import math


class Solution:
    def mySqrt(self, x):
        # also like that
        return int(x ** 0.5)

        ans = math.sqrt(x)
        return int(ans)


ans = Solution()
x = 5
print(ans.mySqrt(x))
