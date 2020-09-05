#双堆栈问题，一个最大堆(堆顶元素大于节点)动态保持流入元素较小一半
#一个最小堆（堆顶元素小于节点）动态保留流入元素较大一半，这样只要最大堆数目和最小堆相等或者多一则最大堆堆顶为所求中位数位置
#进入一个元素先看在最大堆还是最小堆，如果在最大堆但是进入的元素大于最小堆的堆顶交换在置入最大堆，调整最大堆（up down），调整最小堆(down)
#知道父子结点对应关系0，1，2，3，4…… 父 i 左 2*i +1  右2*i+2
#up 向上调整加入的元素 down 向下调整
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

        
