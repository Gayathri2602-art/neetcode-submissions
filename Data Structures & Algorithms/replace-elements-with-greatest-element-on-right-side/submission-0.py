class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        res=[]
        a=[] #2   
        b=[] #4,5,3,1,2  
        for i in range(len(arr)):
            a.append(arr[i])

            for j in range(i+1,len(arr)):
                b.append(arr[j])
            if b:
                res.append(max(b))
            else:
                res.append(-1)
            b=[]
           
        return res
