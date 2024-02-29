class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        semi_cmd = ""
        for ch in path + "/":
            if ch == "/":
                if semi_cmd == "..":
                    if stack:
                        stack.pop()
                elif semi_cmd and semi_cmd != ".":
                    stack.append(semi_cmd)
                semi_cmd = ""
            else:
                semi_cmd += ch
        return "/"+"/".join(stack)