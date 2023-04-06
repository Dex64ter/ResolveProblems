class Solution:
    def isPalindrome(self, s: str) -> bool:
        noalnum = []
        if s != "":
            for i in s:
                if not i.isalnum():
                    if i not in noalnum:
                        noalnum.append(i)
            
            for j in noalnum:
                s = s.replace(j, "")
            s = s.casefold()

        else:
            return True

        return s == ''.join(reversed(s))