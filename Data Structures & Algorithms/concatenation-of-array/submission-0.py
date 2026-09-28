class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n=len(nums)
        ans_len=2*n
        ans_arr=[0]*ans_len
        for i in range(n):
            ans_arr[i]=nums[i]
            ans_arr[i+n]=nums[i]
        self.nums=ans_arr
        return ans_arr


        