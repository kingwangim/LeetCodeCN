# 1096. 花括号展开 II
# brace-expansion-ii

class Solution:
    def braceExpansionII(self, expression: str) -> list[str]:
        def dfs(exp):
            j = exp.find('}')
            if j == -1:
                s.add(exp)
                return
            i = exp.rfind('{', 0, j - 1)
            a, c = exp[:i], exp[j + 1:]
            for b in exp[i + 1: j].split(','):
                dfs(a + b + c)

        s = set()
        dfs(expression)
        return sorted(s)
    
expression = "{a,b}{c,{d,e}}"
print(Solution().braceExpansionII(expression))  