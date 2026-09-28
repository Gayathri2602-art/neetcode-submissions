class Solution:
    def calPoints(self, operations: List[str]) -> int:
        new_arr=[]
        for nums in operations:
            if nums=="+":
                new_arr.append(new_arr[-1]+new_arr[-2])
            elif nums=="D":
                new_arr.append(2*new_arr[-1])
            elif nums=="C":
                new_arr.pop()
            else:
                new_arr.append(int(nums))
        return sum(new_arr)

        