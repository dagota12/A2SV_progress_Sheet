class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        freq1 = Counter(nums1)
        freq2 = Counter(nums2)
        res = []
        # less_elem = nums1 if len(fr) < len(nums2) else nums2
        for e in freq1.keys():
            if e in freq2:
                min_ = min(freq1[e],freq2[e])
                res.extend([e]*min_)
        return res