def romanToInt(s: str) -> int:
  roman_dic = {
      "M": 1000,
      "D": 500,
      "C": 100,
      "L": 50,
      "X": 10,
      "V": 5,
      "I": 1,
  }

  number = 0
  i = 0
  while i < len(s):
    if i+1 != len(s):
      if roman_dic[s[i]] < roman_dic[s[i+1]]:
        number += roman_dic[s[i+1]] - roman_dic[s[i]]
        i += 1
      else:
        number += roman_dic[s[i]]
    else:
      number += roman_dic[s[i]]
    
    i += 1

  return number

print(romanToInt("MCMXCIV"))