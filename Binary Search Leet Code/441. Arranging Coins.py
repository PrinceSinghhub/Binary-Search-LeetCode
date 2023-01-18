class Solution:
    def arrangeCoins(self, n):

        # using Binary Search

        first = 1
        last = n

        while first <= last:

            mid = first + (last - first) // 2

            temp = (mid * (mid + 1) // 2)

            if temp == n:
                return mid

            if temp < n:
                first = mid + 1
            else:
                last = mid - 1
        return last

        # iterative Approch
        Stairs = 1
        while n > 0:
            if n >= Stairs:
                n -= Stairs
                if n == 0:
                    return Stairs
                Stairs += 1
            else:
                return Stairs - 1
ans = Solution()
