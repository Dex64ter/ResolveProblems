def longestCommonPrefix(strs: list[str]) -> str:
  prefix = ""
  equal = min(strs)
  word = True
  print(equal)
  j = 0
  while j < len(equal) and word:
    l = equal[j]
    prefix += l
    for i in strs:
      if i[j] != l:
        word = False
        prefix = prefix[:-1]
        break
    j += 1
  return prefix

print(longestCommonPrefix(["cir","car"]))