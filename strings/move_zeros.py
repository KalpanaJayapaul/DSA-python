"""
Problem: Move Zeros to End
Approach:
- Use a pointer to track position of next non-zero element

Time Complexity: O(n)
Space Complexity: O(1)
"""

def move_zeros(nums):
    pos = 0

    for num in nums:
        if num != 0:
            nums[pos] = num
            pos += 1

    while pos < len(nums):
        nums[pos] = 0
        pos += 1

    return nums


if __name__ == "__main__":
    print(move_zeros([0, 1, 0, 3, 12]))  # [1, 3, 12, 0, 0]
