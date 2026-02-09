"""
Problem: Maximum Subarray Sum (Kadane's Algorithm)
Approach:
- Track current subarray sum and maximum sum

Time Complexity: O(n)
Space Complexity: O(1)
"""

def max_subarray(nums):
    current_sum = max_sum = nums[0]

    for num in nums[1:]:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)

    return max_sum


if __name__ == "__main__":
    print(max_subarray([-2,1,-3,4,-1,2,1,-5,4]))  # 6
