"""
Problem: Reverse a String
Approach:
- Use Python slicing to reverse the string

Time Complexity: O(n)
Space Complexity: O(n)
"""

def reverse_string(s: str) -> str:
    return s[::-1]


if __name__ == "__main__":
    print(reverse_string("hello"))
