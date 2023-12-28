class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        freq = defaultdict(int)
        for cpdomain in cpdomains:
            n,domain = cpdomain.split()
            n = int(n)
            subs = domain.split(".")
            for i in range(len(subs)):
                sub = ".".join(subs[i:])
                freq[sub] += n
        res = []
        for k,v in freq.items():
            res.append(f"{str(v)} {k}")
        return res