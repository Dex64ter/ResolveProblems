def isPalindrome(x: int) -> bool:
  number = list(str(x))
  number_cop = number.copy()
  number.reverse()
  return number == number_cop

print(isPalindrome(121) )