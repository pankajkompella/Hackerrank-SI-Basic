'''
Given N, print the sum of squares of 1st N natural numbers.

Input Format

Input contains positive integer - N.

Constraints

1 <= N <= 103

Output Format

Print the sum of squares of 1st N natural numbers.

Sample Input 0

15
Sample Output 0

1240
Explanation 0

Self Explanatory
'''

n=int(input())
print(n*(n+1)*(2*n+1)//6)
