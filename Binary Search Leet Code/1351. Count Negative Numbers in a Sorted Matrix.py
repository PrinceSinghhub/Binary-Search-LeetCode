# another approch
class Solution1:
    def countNegatives(self, grid):

        ans = 0
        for i in range(len(grid)):

            start = 0
            end = len(grid[i]) - 1

            while start <= end:
                mid = (start + end) // 2
                if grid[i][mid] < 0:
                    end = mid - 1
                else:
                    start = mid + 1
            a = len(grid[i]) - start
            ans += a

        return ans

class Solution:
    def countNegatives(self, grid):

        def count(arr):

            count = 0
            for i in arr:
                if i < 0:
                    count += 1
            return count

        ans = 0
        for i in grid:
            ans += count(i)

        return ans

ans = Solution()
grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
print(ans.countNegatives(grid))
