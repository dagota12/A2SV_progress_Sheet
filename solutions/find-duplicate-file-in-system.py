class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        contents = defaultdict(list)
        for path in paths:
            [dir,*files] = path.split()
            for file_ in files:
                op = file_.find('(')
                name = file_[:op]
                content = file_[op+1:-1]
                contents[content].append(f"{dir}/{name}")
        res = []
        for paths in contents.values():
            if len(paths) > 1:
                res.append(paths)
        return res


