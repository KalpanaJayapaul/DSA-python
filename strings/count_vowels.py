"""
Problem: Count vowels in a string
Approach:
- Iterate through the string and count characters present in vowel set

Time Complexity: O(n)
Space Complexity: O(1)
"""

def count_vowels(s: str) -> int:
    vowels = {'a', 'e', 'i', 'o', 'u'}
    count = 0

    for char in s.lower():
        if char in vowels:
            count += 1

    return count


if __name__ == "__main__":
    print(count_vowels("Hello World"))  # 3
