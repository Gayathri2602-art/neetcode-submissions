class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count=0        #0  1 2 0
        max_cons_ones=[]
        for i in nums:
            if i==1:
                count+=1
            else:
                count=0
            max_cons_ones.append(count)
        return max(max_cons_ones)
        