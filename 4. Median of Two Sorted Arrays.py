class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        len1, len2 = len(nums1), len(nums2)
        if (len1 + len2) % 2 == 1:
            return self.getKth(nums1, nums2, (len1 + len2)/2 + 1)
        else:
            return (self.getKth(nums1, nums2, (len1 + len2)/2) +
                    self.getKth(nums1, nums2, (len1 + len2)/2 + 1)) * 0.5

    def getKth(self, A, B, k):
        m, n = len(A), len(B)
        if m > n:
            return self.getKth(B, A, k)

        left, right = 0, m
        while left < right:
            mid =int(left + (right - left) / 2)
            if 0 <= k - 1 - mid < n and A[mid] >= B[int(k - 1 - mid)]:
                right = mid
            else:
                left = mid + 1

        Ai_minus_1 = A[left - 1] if left - 1 >= 0 else float("-inf")
        Bj = B[int(k - 1 - left)] if k - 1 - left >= 0 else float("-inf")

        return max(Ai_minus_1, Bj)