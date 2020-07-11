'''
Implement binary search. Given a sorted array, search key in the array. If key not found print "false", otherwise print "true".

Input Format

First line of input contains two integers N and K. N is the size of array and K is the key. Second line contains array elements.

Constraints

1 <= N <= 102
0 <= ar[i] <= 109

Output Format

Print "true" if key is present in the array. Otherwise, print false.

Sample Input 0

5 19
2 19 23 35 38
Sample Output 0

true
Explanation 0

Self Explanatory
'''

n,k=map(int,input().split())
arr=list(map(int,input().split()))
lo=0
hi=n-1
# while lo<=hi:
#     mid=(lo+hi)
#     k=
#     if k==
    
def BS(arr,lo,hi,k): 
    if hi>=lo: 
        mid=lo+(hi-lo)//2
        if arr[mid]==k: 
            return mid 
        elif arr[mid]>k: 
            return BS(arr,lo,mid-1,k) 
        else: 
            return BS(arr,mid+1,hi,k) 
    else: 
        return -1
result=BS(arr,0,n-1,k) 

if result!=-1: 
    print("true") 
else: 
    print("false") 
