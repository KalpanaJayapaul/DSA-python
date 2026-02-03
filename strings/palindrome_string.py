"""
Problem: Check if a string is palindrome
Approach:
- Reverse the string and compare with original

Time Complexity: O(n)
Space Complexity: O(n)
"""

def is_palindrome(s: str) -> bool:
    return s == s[::-1]


if __name__ == "__main__":
    print(is_palindrome("madam"))   # True
    print(is_palindrome("hello"))   # False
