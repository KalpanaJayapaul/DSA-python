def longest_k_distinct(s, k):
    left = 0
    char_count = {}
    max_length = 0
    
    for right in range(len(s)):
        char = s[right]
        char_count[char] = char_count.get(char, 0) + 1
        
        # shrink window if more than k distinct chars
        while len(char_count) > k:
            left_char = s[left]
            char_count[left_char] -= 1
            
            if char_count[left_char] == 0:
                del char_count[left_char]
            
            left += 1
        
        max_length = max(max_length, right - left + 1)
    
    return max_length
