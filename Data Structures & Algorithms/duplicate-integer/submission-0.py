class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        res=False
        a=set(nums)
        if len(a)<len(nums):
            res=True
        else:
            res=False
        return res
