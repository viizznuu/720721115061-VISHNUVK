def longestCommonPrefix(strs):
    if not strs:
        return "*"
    prefix = strs[0]
    for s in strs[1:]:
        while not s.startswith(prefix):
            prefix = prefix[:-1]
            if not prefix:
                return "*"
    return prefix

# Input box
strs = input("Enter an array of strings (separated by space): ").split()

print(longestCommonPrefix(strs))