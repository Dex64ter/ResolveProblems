nums = [0,0,1,1,1,2,2,3,3,4]

def removeDuplicates(num: list[int]) -> int:
  global nums
  l = len(num)
  elements = set(num)
  num = list(elements)
  for i in range(l - len(elements)):
    num.append("_")   
  nums = num
  return len(elements)

print(removeDuplicates(nums))
print(nums)