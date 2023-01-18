class Solution(object):
    def maxDistance(self, nums1, nums2):
        def next(arr, target, ind):
            start = ind
            end = len(arr) - 1
            ans = float('-inf')
            while (start <= end):
                mid = (start + end) // 2
                if (arr[mid] < target):
                    end=mid-1
                else:
                    ans=mid
                    start=mid+1
            return ans
        ans=float('-inf')
        for i in range(len(nums1)):
            ans=max(ans, next(nums2, nums1[i], i)-i)
        if ans==float('-inf'):
            return 0
        return ans

ans = Solution()
nums1 = [55,30,5,4,2]
nums2 = [100,20,10,10,5]
print(ans.maxDistance(nums1,nums2))