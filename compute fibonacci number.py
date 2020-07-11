'''
For a given positive integer - N. Compute Nth fibonacci number.

Input Format

Input contains a positive integer - N.

Constraints

1 <= N <= 20

Output Format

For given input, print the Nth fibonacci number.

Sample Input 0

4
Sample Output 0

3
Explanation 0

The fibonacci series:
1, 1, 2, 3, 5, 8,......
At 4th position we have 3.
'''

def Fibonacci(n): 
    if n==0: 
        return 0
    elif n==1: 
        return 1
    else: 
        return Fibonacci(n-1)+Fibonacci(n-2) 
n=int(input())
print(Fibonacci(n)) 
