"""
Problem: Valid Parentheses
Approach:
- Use stack to match opening and closing brackets

Time Complexity: O(n)
Space Complexity: O(n)
"""

def is_valid(s: str) -> bool:
    stack = []
    mapping = {')': '(', '}': '{', ']': '['}

    for char in s:
        if char in mapping.values():
            stack.append(char)
        elif char in mapping:
            if not stack or stack[-1] != mapping[char]:
                return False
            stack.pop()

    return len(stack) == 0


if __name__ == "__main__":
    print(is_valid("()"))      # True
    print(is_valid("(]"))      # False
