def min_window(s, t):
    from collections import Counter, defaultdict
    
    if not s or not t:
        return ""
    
    t_count = Counter(t)
    window_count = defaultdict(int)
    
    required = len(t_count)  # unique chars in t
    formed = 0
    
    left = 0
    right = 0
    min_len = float('inf')
    min_window = (0, 0)
    
    while right < len(s):
        char = s[right]
        window_count[char] += 1
        
        if char in t_count and window_count[char] == t_count[char]:
            formed += 1
        
        # shrink the window from left
        while left <= right and formed == required:
            char = s[left]
            
            if right - left + 1 < min_len:
                min_len = right - left + 1
                min_window = (left, right)
            
            window_count[char] -= 1
            if char in t_count and window_count[char] < t_count[char]:
                formed -= 1
            
            left += 1
        
        right += 1
    
    l, r = min_window
    return s[l:r+1] if min_len != float('inf') else ""
