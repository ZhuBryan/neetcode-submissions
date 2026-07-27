class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2
        total = len(A) + len(nums2)
        half = total // 2

        if len(A) > len(B):
            A, B = B, A
        
        l, r = 0, len(A) - 1
        while True:
            m = (l + r) // 2
            j = half - m - 2

            leftA = A[m] if m >= 0 else float("-infinity")
            rightA = A[m + 1] if (m + 1) < len(A) else float("infinity")
            leftB = B[j] if j >= 0 else float("-infinity")
            rightB = B[j + 1] if (j + 1) < len(B) else float("infinity")

            if leftA <= rightB and leftB <= rightA:
                if total % 2 == 0:
                    return (max(leftA, leftB) + min(rightA, rightB)) / 2
                else:
                    return min(rightA, rightB)
            elif rightB < leftA:
                r = m - 1
            else:
                l = m + 1

