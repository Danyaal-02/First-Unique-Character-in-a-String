def firstUniqChar(s):
    for i in range(len(s)):
        if s[i] not in s[:i] + s[i+1:]:
            return i
    return -1

# Example usage:
s = "leetcode"
print(firstUniqChar(s))  # Output: 0

s = "loveleetcode"
print(firstUniqChar(s))  # Output: 2

s = "aabbcc"
print(firstUniqChar(s))  # Output: -1
