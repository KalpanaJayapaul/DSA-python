"""
Problem: Check if two strings are anagrams
Approach:
- Convert both strings to lowercase
- Sort both strings and compare

Time Complexity: O(n log n)
Space Complexity: O(n)
"""

def is_anagram(s1: str, s2: str) -> bool:
    return sorted(s1.lower()) == sorted(s2.lower())


if __name__ == "__main__":
    print(is_anagram("listen", "silent"))  # True
    print(is_anagram("hello", "world"))    # False
