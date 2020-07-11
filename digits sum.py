'''
Given non-negative integer - N, print the sum of digits of the given number.

Input Format

Input contains non-negative integer - N.

Constraints

0 <= length(N) <= 103

Output Format

Print the sum of digits of the given number.

Sample Input 0

164
Sample Output 0

11
Explanation 0

Self Explanatory
'''

number=int(input())
addition=0
modulo=0
while number!=0:
    modulo=number%10
    addition+=modulo
    number//=10
print(addition)
