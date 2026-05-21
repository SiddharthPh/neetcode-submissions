class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        getposandvalue = self.finmaxvalueandposition(0, arr)
        pos = getposandvalue[0]
        maxvalue = getposandvalue[1]
        for i in range(len(arr)):
            if i < pos:
                arr[i]=maxvalue
            elif i==pos:
                pos=self.finmaxvalueandposition(i+1, arr)[0]
                maxvalue=self.finmaxvalueandposition(i+1, arr)[1]
                arr[i]=maxvalue
        arr[-1]=-1
        return arr

    def finmaxvalueandposition(self, initpos, arr):
        maxvalue = float('-inf')
        pos=initpos
        for i in range(initpos, len(arr)):
            if(arr[i]>maxvalue):
                maxvalue=arr[i]
                pos=i
        return [pos, maxvalue]

        
