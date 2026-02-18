"""
Problem: Longest Repeating Character Replacement
Approach:
- Sliding window with frequency map
- Maintain max frequency inside window

Time Complexity: O(n)
Space Complexity: O(1)  # Only 26 uppercase letters
"""

def character_replacement(s: str, k: int) -> int:
    count = {}
    left = 0
    max_freq = 0
    max_length = 0

    for right in range(len(s)):
        count[s[right]] = count.get(s[right], 0) + 1
        max_freq = max(max_freq, count[s[right]])

        while (right - left + 1) - max_freq > k:
            count[s[left]] -= 1
            left += 1

        max_length = max(max_length, right - left + 1)

    return max_length


if __name__ == "__main__":
    print(character_replacement("AABABBA", 1))  # 4
