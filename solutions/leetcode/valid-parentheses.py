class Solution:
    def isValid(self, s: str) -> bool:
        if len(s)%2 != 0:
            return False
        val=[]
        brace={"}":"{","]":"[",")":"("}
        open='{[('
        for i in s:
            if i in open:
                val.append(i)
            elif val==[]:
                return False
            else:
                if brace[i] == val[-1]:
                    val.pop()
                else:return False
        return val==[]