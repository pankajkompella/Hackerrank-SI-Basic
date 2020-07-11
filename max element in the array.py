'''
Find maximum element from the given array of integers.

Input Format:
First line of input contains N - the size of the array and second line contains the elements of the array.
Constraints:
1 <= N <= 103
-109 <= ar[i] <= 109
Output Format:
Print the maximum element of array.

Sample Input 0:
5
-2 -19 8 15 4
Sample Output 0:
15
Explanation 0:
Self Explanatory
'''

n=int(input())
temp=0
a=list(map(int,input().split()))
for i in range(n):
    for j in range(i+1,n):
        if a[i]>a[j]:
            temp=a[i]
            a[i]=a[j]
            a[j]=temp
print(a[j])
