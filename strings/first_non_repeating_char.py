"""
Problem: First non-repeating character in a string
Approach:
- Count frequency of characters using dictionary
- Traverse string to find first character with count 1

Time Complexity: O(n)
Space Complexity: O(n)
"""

def first_non_repeating_char(s: str):
    freq = {}

    for char in s:
        freq[char] = freq.get(char, 0) + 1

    for char in s:
        if freq[char] == 1:
            return char

    return -1


if __name__ == "__main__":
    print(first_non_repeating_char("swiss"))  # w
    print(first_non_repeating_char("aabb"))   # -1
