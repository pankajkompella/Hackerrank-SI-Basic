'''
Given two integers a and b. compute a power b.

Input Format

Input contains two positive integers a and b.

Constraints

1 <= a <=100
0 <= b <=9

Output Format

Print a power b.

Sample Input 0

2 3
Sample Output 0

8
Explanation 0

Self Explanatory.
'''

b,e=map(int,input().split())
print(pow(b,e))
