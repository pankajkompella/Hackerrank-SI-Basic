'''
Print unique elements of the array in the same order as they appear in the input.
Note: Do not use any inbuilt functions/libraries for your main logic.

Input Format:
First line of input contains a single integer N - the size of array and second line contains array elements.

Constraints:
1 <= N <= 100
0 <= ar[i] <= 109

Output Format:
Print unique elements of the array.

Sample Input 0:
7
5 4 10 9 21 4 10

Sample Output 0:
5 9 21

Explanation 0:
Self Explanatory.
'''

n=int(input())
c=[]
a=list(map(int,input().split()))
for i in range(n):
    b=a.count(a[i])
    if(b==1):
        c.append(a[i])
for k in c:
    print(k,end=" ")
