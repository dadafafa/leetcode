class Solution:
    """
    @param nums: A list of integers
    @return: the median of numbers
    """
    def medianII(self, nums):
        # write your code here
        lenth= len(nums)
        if lenth==0:
            return []
        maxheap=[]
        minheap=[]
        result=[]
        for i in nums:
            result.append(self.add(i,maxheap,minheap))
            print(maxheap,minheap,i)
        return result
    
    def add(self,target,maxheap,minheap):
        if maxheap==[]:
            maxheap.append(target)
            return target
        if len(maxheap)>len(minheap):
            #add min
            if target<maxheap[0]:
                maxheap[0],target=target,maxheap[0]
                self.down(maxheap,"max")
                self.addtoheap(minheap,target,"min")
                #adjust max
                #add min
            else: 
                self.addtoheap(minheap,target,"min")
                #add min
        else:
            if target>minheap[0]:
                minheap[0],target=target,minheap[0]
                self.down(minheap,"min")
                self.addtoheap(maxheap,target,"max")
            else:
                self.addtoheap(maxheap,target,"max")
            #add max
        return maxheap[0]
    def addtoheap(self,A,nums,tag):
        A.append(nums)
        self.up(A,tag)
        self.down(A,tag)
    def up(self,A,tag):
        n=len(A)-1
        father=int((n-1)/2)
        if tag=="max":
            while n!=0 and A[father]<A[n]:
                A[father],A[n]=A[n],A[father]
                n=father
                father= int((n-1)/2)
        if tag=="min":
            while n!=0 and A[father]>A[n]:
                A[father],A[n]=A[n],A[father]
                n=father
                father= int((n-1)/2)
    def down(self,A,tag):
        if A[0]==2:
            print(A,tag)
        length=len(A)-1
        n=0
        if tag=="max":
            while n<length:
              
                lc,rc=2*n+1,2*n+2
                if lc<length and rc<length:
                    if A[n] <max(A[lc],A[rc]):
                        tem = lc if A[lc]>A[rc] else rc
                        A[tem],A[n] = A[n],A[tem]
                        n = tem
                    else:
                        break
                elif rc>length and lc<=length and  A[n]<A[lc]  :
                    A[n],A[lc]=A[lc],A[n]
                    n=lc
                    break
                else:
                    break
        if tag=="min":
            while n<length:
                lc,rc=2*n+1,2*n+2
                if lc<length and rc<length:
                    if A[n] >min(A[lc],A[rc]):
                        tem = lc if A[lc]<A[rc] else rc
                        A[tem],A[n] = A[n],A[tem]
                        n=tem
                    else:
                        break
                elif rc>length and lc<=length and A[n]>A[lc] :
                    A[n],A[lc]=A[lc],A[n]
                    n=lc
                else:
                    break

        
