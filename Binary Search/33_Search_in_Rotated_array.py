class Solution:
    def search(self, nums: List[int], target: int) -> int:
        ### Three pass solution (O3logn)
        
        # Find smallest number using binary search
        # We know the num to the left (immediate) is the largest
        # Now we have the lower and upper bounds for the binary search
        # Conduct regular binary search until num is found
        smlIndex = -1
        left = 0
        n = len(nums)
        right = n-1

        while left < right:
            mid = (left + right) // 2
            leftSum = nums[left] - nums[mid]
            rightSum = nums[mid] - nums[right]
            leftIdx = (mid - 1) % n
            if nums[leftIdx] > nums[mid]:
                smlIndex = mid
                break

            if leftSum >= rightSum:
                # search left half
                right = mid - 1
            else:
                left = mid + 1
        
        if smlIndex == -1: smlIndex = left

        pivot = (smlIndex - 1) % n

        def search(left, right) -> int:
            leftP = left
            rightP = right
            result = -1
            while leftP <= rightP:
                index = (leftP + rightP) // 2
                if (nums[index]) == target:
                    result = index
                    break
                elif (nums[index]) > target:
                    rightP = index - 1
                else:
                    leftP = index + 1
            
            return result
        
        # Just run binary searches on each of the sorted arrays, and return the result.
        res = search(0, pivot)
        if res == -1:
            return search(pivot + 1, n-1)
        
        return res
    

        ### One pass solution
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid

            # Left half is sorted
            if nums[left] <= nums[mid]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1  # target in the left sorted part
                else:
                    left = mid + 1   # target in the right rotated part

            # Right half is sorted
            else:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1   # target in the right sorted part
                else:
                    right = mid - 1  # target in the left rotated part

        return -1