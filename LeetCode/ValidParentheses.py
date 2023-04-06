class Solution:
    def isValid(self, s: str) -> bool:
        closed_bars = {
            ")": "(",
            "}": "{",
            "]": "[",
        }
        
        if len(s) == 1:
            return False

        pilha = []
        for bar in s:
            if bar in closed_bars:
                if pilha:
                    if closed_bars[bar] == pilha[-1]:
                        pilha.pop()
                    else:
                        return not pilha
                else:
                    return False
            else:
                pilha.append(bar)
        # 
        return not pilha