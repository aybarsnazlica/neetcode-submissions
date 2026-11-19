class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge(nums, left, mid, right):
            left_half = nums[left : mid + 1]
            right_half = nums[mid + 1 : right + 1]

            i, j, k = left, 0, 0

            while j < len(left_half) and k < len(right_half):
                if left_half[j] <= right_half[k]:
                    nums[i] = left_half[j]
                    j += 1
                else:
                    nums[i] = right_half[k]
                    k += 1
                i += 1

            while j < len(left_half):
                nums[i] = left_half[j]
                j += 1
                i += 1

            while k < len(right_half):
                nums[i] = right_half[k]
                k += 1
                i += 1

        def merge_sort(nums, left, right):
            if left >= right:
                return

            mid = (left + right) // 2
            merge_sort(nums, left, mid)
            merge_sort(nums, mid + 1, right)
            merge(nums, left, mid, right)

        merge_sort(nums, 0, len(nums) - 1)
        return nums
