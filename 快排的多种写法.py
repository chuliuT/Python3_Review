import numpy as np

def QuickSort(arr,l,r):
    """
    主函数的功能是  选取一个基准的值  然后将小于基准值的 全部放左边   比它大的值不用管
    依次对比arr[0]和其他元素，比arr[0]小的话，就原地删除，然后插入到arr[0]前面（这一步其实是跟扑克牌的插入有点像，
    但是不会考虑前面牌的顺序），基准值后移。大于等于，则不处理。然后递归
    :param arr:
    :param l:
    :param r:
    :return:
    """
    if l>r: return
    pivot_idx=l
    for i in range(l+1,r+1):
        if arr[pivot_idx]>arr[i]:
            temp=arr[i]
            del arr[i]
            arr.insert(pivot_idx,temp)
            pivot_idx+=1
    QuickSort(arr,l,pivot_idx-1)
    QuickSort(arr,pivot_idx+1,r)

def QuickSort2(arr):
    """
    按基准值，两边排。。。小的在左边   大的在右边  （不管顺序） 然后递归
    :param arr:
    :return:
    """
    if len(arr)<=1: return arr
    pivot=len(arr)//2
    left =[x for x in arr if x<arr[pivot]]
    mid=[x for x in arr if x==arr[pivot]]
    right=[x for x in arr if x>arr[pivot]]
    return QuickSort2(left)+mid+QuickSort2(right)

def QuickSort22(arr):
    """
    #2）基准值arr[0]，对比所有元素，比它小就追加到less后面，
    比它大就追加到great后面，相等就追加到pivot后面，然后递归
    :param arr:
    :return:
    """
    left=[]
    mid=[]
    right=[]
    if len(arr)<=1:
        return arr
    else:
        p=arr[0]
        for i in arr:
            if i<p:
                left.append(i)
            elif i>p:
                right.append(i)
            else:
                mid.append(i)
        return QuickSort22(left)+ mid + QuickSort22(right)

quick_sort23=lambda arr:arr if len(arr)<=1 else quick_sort23([x for x in arr[1:] if x<arr[0]])+[arr[0]]+quick_sort23([x for x in arr[1:] if x>arr[0]])


#########################################
#写一个partition的函数用于分区。。
#########################################

def partition(arr,left,right):
    """
    定义两个函数：分区和排序。分区是要把列表元素移动位置，
    直到基准值arr[0]移到中间（左边都比它小，右边都比它大）。
    排序则调用分区并递归
    :param arr:
    :param left:
    :param right:
    :return:
    """
    p=arr[left]
    while left!=right:
        while left<right and p<=arr[right]:
            right-=1
        arr[left]=arr[right]
        while left<right and p>arr[left]:
            left+=1
        arr[right]=arr[left]
    arr[left]=p
    return left

def partition2(arr,l,r):
    p=arr[l]
    while l!=r:
        while l<r and p<=arr[r]:
            r-=1
        while l<r and p>arr[r]:
            arr[l]=arr[r]
            l+=1
            arr[r]=arr[l]
    arr[l]=p
    return l

def partition3(arr,l,r):
    p=arr[r]
    i=l-1
    for j in range(l,r):
        if arr[j]<=p:
            i+=1
            arr[i],arr[j]=arr[j],arr[i]
    arr[i+1],arr[r]=arr[r],arr[i+1]
    return i+1



def QuickSort3(arr,l,r):
    if len(arr)<=1: return arr
    if l<r:
        pi=partition3(arr,l,r)
        QuickSort3(arr,l,pi-1)
        QuickSort3(arr,pi+1,r)
    return arr






if __name__ == '__main__':
    s = np.random.randint(1, 30, 20).tolist()
    print(s)
    # QuickSort(s, 0, len(s) - 1)
    # ans=quick_sort23(s)
    # print(ans)
    ans=QuickSort3(s,0,len(s)-1)
    print(ans)
