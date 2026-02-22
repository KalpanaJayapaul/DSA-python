def group_anagrams(strs):
    from collections import defaultdict
    
    anagram_map = defaultdict(list)
    
    for word in strs:
        count = [0] * 26
        
        for char in word:
            count[ord(char) - ord('a')] += 1
        
        key = tuple(count)
        anagram_map[key].append(word)
    
    return list(anagram_map.values())
